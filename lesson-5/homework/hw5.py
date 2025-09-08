1.date=int(input('Enter your date here:')) 
if date%4==0 and (date%100!=0 or date%400==0): 
    print('It is leap year') 
else: 
    print('It is not leap year') 
2.n=int(input('Enter the number here:3')) 
if n>=1 and n<=100:
    if n%2==1: 
     print('Weird') 
    if n>=2 and n<=5 and n%2==0: 
     print ('Not weird') 
    if n>=6 and n<=20 and n%2==0: 
        print('Weird') 
    if n>20 and n%2==0: 
        print('Not weird') 
3.1 
a = int(input())
b = int(input())

# Find first even number >= a
if a % 2 == 0:
    first_even = a
else:
    first_even = a + 1

# Find last even number <= b
if b % 2 == 0:
    last_even = b
else:
    last_even = b - 1

# Calculate number of even terms
if first_even > last_even:
    print([])
else:
    n = ((last_even - first_even) // 2) + 1
    # Generate list using sum of arithmetic progression
    evens = [first_even + 2*i for i in range(n)]
    print(evens) 
  2.
a = int(input())
b = int(input())

# Mathematical approach without any conditionals
first_even = a + (a % 2)
last_even = b - (b % 2)

# Number of terms (0 if no even numbers exist)
n = max(0, (last_even - first_even) // 2 + 1)

# Generate the sequence using arithmetic progression formula
# Create list by adding multiples of 2 to first_even
evens = list(map(lambda i: first_even + 2*i, range(n)))
print(evens)



