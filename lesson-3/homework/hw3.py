1.my_list=['apple', 'banana', 'orange', 'grapes', 'pineapple'] 
print(my_list[2]) 
2.numbers1=[1,3,20] 
numbers2=[5,7,22] 
x=numbers1+numbers2 
print(x) 
3.numbers1=[1,3,20] 
first, *middle, last = numbers1
print(first) 
print(middle) 
print(last)
4.my_favourite_films=['harry potter', 'Avangers', 'Thore', 'Iron man', 'Spiderman'] 
tuple(my_favourite_films)
5.Cities = ["Paris", "London", "Tashkent", "Istanbul"]
print("Paris" in Cities) 
6.numbers = [1, 2, 3, 4, 5]
duplicate = numbers * 2
print(duplicate) 
7.numbers = [111, 12, 123, 222, 454] 

first=numbers[0] 
last=numbers[-1] 

numbers[0]=last 
numbers[-1]=first 
print(numbers) 
8. numbers_tuple=(1,2,3,4,5,6,7,8,9,10) 
result=numbers_tuple[3:8] 
print(result) 
9. colours=['black', 'blue', 'blue', 'red', 'white'] 
colours.count('blue') 
10. animals=('lion', 'rabbit', 'cat', 'cow') 
animals.index('lion') 
11.number1=(1,2,3) 
number2=(4,5,6) 
single_tuple=(number1+number2) 
print(single_tuple)  
12.number1=(1,2,3) 
number2=[4,5,6,8] 
print(len(number1))
print(len(number2)) 
13.number1=(1,2,3,4,5) 
number2=list(number1) 
print(number2) 
14.number1=(1,2,3,4,5) 
max_value=max(number1) 
min_value=min(number1)
print(max_value)
print(min_value) 
15.colours=('black', 'blue', 'blue', 'red', 'white')
result=tuple(reversed(colours))
print(result)
