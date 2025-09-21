1.n = int(input('number here: '))

def is_prime(n):
    if n <= 1:
        return False
    
    # 2 dan n-1 gacha barcha sonlarga bo'linishini tekshiramiz
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

result = is_prime(n)
print(result) 
2.k=input('number here:')
def digit_sum(k):
    cnt=0 
    for digit in str(k): 
        cnt+=int(digit) 
    return cnt 
result=digit_sum(k)
print(result)
3.n = int(input('enter number here: '))

def my_function(n):
    if n <= 0:
        return False
    
    daraja = 0
    result = 1
    
    # result n dan oshmaguncha davom etamiz
    while result <= n:
        print(result)
        daraja += 1
        result = 2 ** daraja

my_function(n)
