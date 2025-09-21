import threading
import math

def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for factors up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_primes_in_range(start, end, primes_list, lock):
    """Check for primes in a given range and add to shared list"""
    local_primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            local_primes.append(num)
    
    # Use lock to safely update the shared list
    with lock:
        primes_list.extend(local_primes)

def threaded_prime_checker(start_range, end_range, num_threads=4):
    """Main function to check primes using multiple threads"""
    primes = []
    lock = threading.Lock()
    threads = []
    
    # Calculate range for each thread
    total_numbers = end_range - start_range + 1
    numbers_per_thread = total_numbers // num_threads
    
    # Create and start threads
    for i in range(num_threads):
        thread_start = start_range + i * numbers_per_thread
        thread_end = thread_start + numbers_per_thread - 1
        
        # Last thread gets any remaining numbers
        if i == num_threads - 1:
            thread_end = end_range
        
        thread = threading.Thread(
            target=check_primes_in_range,
            args=(thread_start, thread_end, primes, lock)
        )
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return sorted(primes)

def main():
    print("=== Threaded Prime Number Checker ===")
    
    # Get user input
    try:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        num_threads = int(input("Enter number of threads (default 4): ") or 4)
        
        if start > end:
            print("Error: Start must be less than or equal to end")
            return
        
        if num_threads < 1:
            print("Error: Number of threads must be at least 1")
            return
        
    except ValueError:
        print("Error: Please enter valid integers")
        return
    
    # Find primes using multiple threads
    print(f"\nChecking primes from {start} to {end} using {num_threads} threads...")
    primes = threaded_prime_checker(start, end, num_threads)
    
    # Display results
    print(f"\nFound {len(primes)} prime numbers:")
    print(primes)
    
    # Show some statistics
    if primes:
        print(f"\nLargest prime: {primes[-1]}")
        print(f"Smallest prime: {primes[0]}")
    else:
        print("No prime numbers found in the given range.")

if __name__ == "__main__":
    main() 
2.import threading
import re
from collections import defaultdict

def process_chunk(lines, word_count, lock):
    """Process a chunk of lines and count words"""
    local_count = defaultdict(int)
    
    for line in lines:
        # Clean and split into words
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            local_count[word] += 1
    
    # Update global count safely
    with lock:
        for word, count in local_count.items():
            word_count[word] += count

def threaded_word_counter(filename, num_threads=4):
    """Main function to count words using multiple threads"""
    word_count = defaultdict(int)
    lock = threading.Lock()
    threads = []
    
    try:
        # Read the entire file
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
    if not lines:
        print("File is empty")
        return word_count
    
    # Calculate lines per thread
    total_lines = len(lines)
    lines_per_thread = total_lines // num_threads
    
    # Create and start threads
    for i in range(num_threads):
        start_idx = i * lines_per_thread
        end_idx = start_idx + lines_per_thread
        
        # Last thread gets remaining lines
        if i == num_threads - 1:
            end_idx = total_lines
        
        chunk = lines[start_idx:end_idx]
        
        thread = threading.Thread(
            target=process_chunk,
            args=(chunk, word_count, lock)
        )
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return dict(word_count)

def generate_sample_file(filename, num_lines=1000):
    """Generate a sample text file for testing"""
    sample_text = """Python is a programming language that lets you work quickly
    and integrate systems more effectively. Python is easy to learn and powerful
    programming language. It has efficient high-level data structures and a simple
    but effective approach to object-oriented programming. Python's elegant syntax
    and dynamic typing, together with its interpreted nature, make it an ideal
    language for scripting and rapid application development in many areas on
    most platforms. The Python interpreter and the extensive standard library
    are freely available in source or binary form for all major platforms from
    the Python web site. Python is wonderful and amazing language for developers."""
    
    words = sample_text.split()
    
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(num_lines):
            # Create some variation in the text
            line = ' '.join(words[:len(words)//2]) + f" line {i+1} "
            line += ' '.join(words[len(words)//2:]) + "\n"
            file.write(line)
    
    print(f"Generated sample file '{filename}' with {num_lines} lines")

def main():
    print("=== Threaded File Word Counter ===")
    
    filename = input("Enter filename (or press Enter for sample.txt): ").strip()
    if not filename:
        filename = "sample.txt"
        generate_sample_file(filename, 5000)
    
    try:
        num_threads = int(input("Enter number of threads (default 4): ") or 4)
        if num_threads < 1:
            print("Number of threads must be at least 1")
            return
    except ValueError:
        print("Invalid input, using 4 threads")
        num_threads = 4
    
    print(f"\nProcessing '{filename}' using {num_threads} threads...")
    
    # Count words using multiple threads
    word_count = threaded_word_counter(filename, num_threads)
    
    if word_count is None:
        return
    
    # Display results
    print(f"\nFound {len(word_count)} unique words")
    print(f"Total words: {sum(word_count.values())}")
    
    # Show top 20 most common words
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    print("\nTop 20 most common words:")
    print("-" * 30)
    for i, (word, count) in enumerate(sorted_words[:20], 1):
        print(f"{i:2d}. {word:15s}: {count:4d}")
    
    # Show some statistics
    print(f"\nUnique words: {len(word_count)}")
    print(f"Total word occurrences: {sum(word_count.values())}")
    
    # Save results to file
    output_file = "word_count_results.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Word Count Results\n")
        f.write("=" * 50 + "\n")
        for word, count in sorted(word_count.items()):
            f.write(f"{word:20s}: {count:6d}\n")
    
    print(f"\nDetailed results saved to '{output_file}'")

# Alternative: Single-threaded version for comparison
def single_threaded_word_counter(filename):
    """Single-threaded version for performance comparison"""
    word_count = defaultdict(int)
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = re.findall(r'\b\w+\b', line.lower())
                for word in words:
                    word_count[word] += 1
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    
    return dict(word_count)

if __name__ == "__main__":
    main()
    
    # Uncomment to compare performance
    """
    import time
    print("\n" + "="*50)
    print("PERFORMANCE COMPARISON")
    print("="*50)
    
    filename = "sample.txt"
    
    # Multi-threaded
    start_time = time.time()
    threaded_result = threaded_word_counter(filename, 4)
    threaded_time = time.time() - start_time
    
    # Single-threaded
    start_time = time.time()
    single_result = single_threaded_word_counter(filename)
    single_time = time.time() - start_time
    
    print(f"Multi-threaded time: {threaded_time:.3f} seconds")
    print(f"Single-threaded time: {single_time:.3f} seconds")
    print(f"Speedup: {single_time/threaded_time:.2f}x")
    
    # Verify results are the same
    if threaded_result == single_result:
        print("✓ Results match between threaded and single-threaded versions")
    else:
        print("✗ Results differ between versions")
    """
