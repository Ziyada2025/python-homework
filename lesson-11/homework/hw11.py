1.# Create virtual environment
!python -m venv myenv

# Install packages (Windows)
!myenv\\Scripts\\pip install numpy pandas requests matplotlib 
2.def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide a by b and return the result.
    Returns None if division by zero is attempted."""
    if b == 0:
        return None
    return a / b 
2.1def reverse_string(s):
    """Reverse a string and return the result."""
    return s[::-1]

def count_vowels(s):
    """Count the number of vowels in a string and return the count."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count 
3.import geometry
import file_operations

print(geometry.calculate_area(10))
print(file_operations.read_file("test.txt"))

# Method 2: Import specific modules
from geometry.circle import calculate_area
from file_operations.file_reader import read_file

print(calculate_area(7))
print(read_file("data.txt"))
