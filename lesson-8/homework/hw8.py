1.try:
        surat=int(input('Enter your number here:')) 
        mahraj=int(input('Enter your number here')) 
        result=surat/mahraj 
except ZeroDivisionError: 
        print('Error: The number cant be divided to zero value') 
2.try: 
    x=int(input('Enter your integer here')) 
except ValueError: 
    print('Error:Your value is not integer') 
3.try: 
    with open ('example.txt', 'r') as file_handler: 
        print(file_handler.read()) 
except FileNotFoundError: 
    print('An error occured') 
4.try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: ")) 
except ValueError: 
    print('Error:You dont use numerical data') 
5. try: 
    with open ('example.txt', 'r') as file_handler: 
        print(file_handler.read()) 
except PermissionError: 
    print('An permission error occured')  
6.
my_list = [10, 20, 30, 40, 50]
    
try:
    index = int(input("Enter index to access from 0-4: ")) 
    print(my_list[index])
except IndexError:
    print("Error: Index is out of range! 0-4") 
7.try:
    while True:
        name = input("Enter your name (Ctrl+C to quit): ")
        print(f"Hello, {name}!")
except KeyboardInterrupt:
    print("\n\nGoodbye! Program stopped by user.") 
8.try:
    result = 10 / 0
except ArithmeticError as e:
    print(f"Math error occurred: {e}") 
9.
try:
    byte_data = b'hello world'
    result = byte_data.decode('ascii')  # This works
    print(result)
    
    # This will cause UnicodeDecodeError
    result = byte_data.decode('utf-16')
    
except UnicodeDecodeError as e:
    print(f"Decoding failed: {e}") 
10.
try:
    my_list = [1, 2, 3] 
    my_list.get[5] 
except AttributeError: 
    print('Eroor: There is nor this number in list') 
1.with open ('C:\\Users\\Ziyada\\Desktop\\МААБ\\python\\New Text Document.txt') as file: 
    print(file.read()) 
2.with open('C:\\Users\\Ziyada\\Desktop\\МААБ\\python\\New Text Document.txt') as f:
  print(f.readline())
3.with open ('C:\\Users\\Ziyada\\Desktop\\МААБ\\python\\New Text Document.txt', 'a') as file: 
   file.write('Now its appended') 
4.file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
n = 5

with open(file_path, 'r') as file:
    lines = file.readlines()
    last_lines = lines[-n:]
    
for line in last_lines:
    print(line.strip()) 
5.file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
with open(file_path, 'r') as file:
    lines_list = file.readlines()
print("Lines stored in list:", lines_list) 
6.file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
with open(file_path, 'r') as file:
    file_content = file.read()
print("File content stored in variable:", file_content) 
7.file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
lines_array = []
with open(file_path, 'r') as file:
    for line in file:
        lines_array.append(line.strip())
print("Lines stored in array:", lines_array) 
8.file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
with open(file_path, 'r') as file:
    content = file.read()
    words = content.replace(',', ' ').split()
    longest_word = max(words, key=len)
    longest_words = [word for word in words if len(word) == len(longest_word)]
print("Longest word(s):", longest_words) 
9.file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
with open(file_path, 'r') as file:
    line_count = sum(1 for line in file)
print("Number of lines:", line_count) 
10.file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
from collections import Counter
with open(file_path, 'r') as file:
    content = file.read()
    words = content.lower().replace(',', ' ').replace('.', ' ').split()
    word_count = Counter(words)
print("Word frequency:", word_count.most_common(10)) 
11.import os
file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
file_size = os.path.getsize(file_path)
print("File size:", file_size, "bytes") 
12.file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\output.txt'
my_list = ['apple', 'banana', 'cherry', 'date']
with open(file_path, 'w') as file:
    for item in my_list:
        file.write(item + '\n')
print("List written to file") 
13.source_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
dest_path = r'C:\Users\Ziyada\Desktop\МААБ\python\copy.txt'
with open(source_path, 'r') as source, open(dest_path, 'w') as dest:
    dest.write(source.read())
print("File copied successfully") 
14.file1_path = r'C:\Users\Ziyada\Desktop\МААБ\python\file1.txt'
file2_path = r'C:\Users\Ziyada\Desktop\МААБ\python\file2.txt'
output_path = r'C:\Users\Ziyada\Desktop\МААБ\python\combined.txt'

with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2, open(output_path, 'w') as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    for line1, line2 in zip(lines1, lines2):
        out.write(f"{line1.strip()} | {line2.strip()}\n")
print("Files combined") 
15.import random
file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
    random_line = random.choice(lines).strip()
print("Random line:", random_line) 
16.file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
file = open(file_path, 'r')
print("File closed before reading?", file.closed)
content = file.read()
file.close()
print("File closed after reading?", file.closed) 
17.file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
output_path = r'C:\Users\Ziyada\Desktop\МААБ\python\no_newlines.txt'

with open(file_path, 'r') as infile, open(output_path, 'w') as outfile:
    content = infile.read()
    content_no_newlines = content.replace('\n', ' ')
    outfile.write(content_no_newlines)
print("Newlines removed and saved to new file") 
18.file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
with open(file_path, 'r') as file:
    content = file.read()
    words = content.replace(',', ' ').split()
    word_count = len(words)
print("Number of words:", word_count) 
19.file_path = r'C:\Users\Ziyada\Desktop\МААБ\python\New Text Document.txt'
char_list = []
with open(file_path, 'r') as file:
    content = file.read()
    char_list = list(content.replace('\n', '').replace(' ', ''))
print("Characters extracted:", char_list[:20])  # Show first 20 chars 
20.import os
folder_path = r'C:\Users\Ziyada\Desktop\МААБ\python\alphabet_files'
os.makedirs(folder_path, exist_ok=True)

for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    file_path = os.path.join(folder_path, f'{letter}.txt')
    with open(file_path, 'w') as file:
        file.write(f"This is file {letter}.txt\n")
print("26 alphabet files created") 
21.output_path = r'C:\Users\Ziyada\Desktop\МААБ\python\alphabet.txt'
letters_per_line = 5

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open(output_path, 'w') as file:
    for i in range(0, len(alphabet), letters_per_line):
        line = ' '.join(alphabet[i:i+letters_per_line])
        file.write(line + '\n')
print("Alphabet file created with", letters_per_line, "letters per line")
