1.name='John' 
age=18 
print(f'Hello {name}, you are {age} years old') 
2.print(txt[::2]) 
print(txt[1::2]) 
3.print(txt[0::2]) 
print(txt[-1::-2]) 
4.txt[21:] 
5.txt='input_string' 
print(txt[-1::-1]) 
6.text = ("Ziyada").lower()
count = 0

for letter in text:
    if letter in "aeiou":
        count += 1

print("Vowels:", count) 
7.x=[10,222,244,343] 
max_value=max(x)
print(max_value) 
8.txt = 'ziyada'

if txt == txt[::-1]:
    print(f'The {txt} is palindrome') 
else:
    print(f'{txt} not palindrome')  
  9.email = "ziyada.acca@gmail.com"
result = email.split('@')[0]
print(result) 
10. import random, string
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#"
password = ''.join(random.choice(chars) for i in range(10))
print(password)
