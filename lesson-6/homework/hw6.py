1. 
txt = "abcabcabcdeabcdefabcdefg"
vowels = "aeiouAEIOU"
result = []
i = 0

while i < len(txt):
    # Take 3 characters
    if i + 3 <= len(txt):
        # Add the 3 characters
        result.append(txt[i])
        result.append(txt[i+1])
        result.append(txt[i+2])
        i += 3
        
        # Check if last character added was a vowel
        # If yes, keep adding until non-vowel
        while i < len(txt) and result[-1] in vowels:
            result.append(txt[i])
            i += 1
        
        # Add underscore if not at the end
        if i < len(txt):
            result.append('_')
    else:
        # Add remaining characters
        while i < len(txt):
            result.append(txt[i])
            i += 1

output = ''.join(result)
print(output)
2.
i=0
while  i < n: 
 print(i**2) 
 i=i+1 
n=int(input('Enter your number:')) 
3.1
n=1 
while n<11: 
    print(n) 
    n=n+1 
3.2 
n = 10
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
3.3 x=int(input('enter your number:'))
sum=0
for num in range (x): 
    sum+=num
print(sum) 
4. n=0
while n<22: 
    print(n) 
    n+=2

5.numbers = [12, 75, 150, 180, 145, 525, 50] 
selected_numbers=[75, 150,145]
for num in numbers: 
    if num in selected_numbers: 
        print(num)
6.x=75869
print('Total character:', len(str(x))) 
7.
n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print() 
8.
list1 = [10, 20, 30, 40, 50] 
for item in reversed(list1): 
    print(item) 
9.
n=-10 
while n<0: 
    print(n) 
    n=n+1 
10.
n=0 
while n<10: 
    if n==5: 
        print('Done') 
        break 
    print(n) 
    n+=1 
11.
for num in range(25,50):
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True
        for i in range(2, num):  # Check divisibility from 2 to num-1
            if num % i == 0:     # If divisible by any number
                is_prime = False
                break
        if is_prime:
            print(num, end=" ") 
12. 
n_terms = 10
a, b = 0, 1

print("Fibonacci series up to 10 terms:")
for i in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b 
13.
num=5
if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0 or num == 1:
    print(f"The factorial of {num} is 1")
else:
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}") 
  14.
list1 = [1, 1, 2]
list2 = [2, 3, 4]
result = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
print(result)  # Output: [1, 1, 3, 4]
