1.my_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1}

# Ascending order (lowest to highest)
ascending = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("Ascending:", ascending)

# Descending order (highest to lowest)
descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Descending:", descending)
2.dictionary={0: 10, 1: 20} 
dictionary.update({2:30}) 
print(dictionary) 
3.dic1.update(dic2) 
dic1.update(dic3) 
new_updated_dic=dic1 
print(new_updated_dic) 
4.n = 5
squares = {}
for x in range(1, n+1):
    squares[x] = x * x
print(squares) 
5.n = 15
squares = {}
for x in range(1, n+1):
    squares[x] = x * x
print(squares) 
SET EXERCISES 
1.my_set={'a', 'b', 'c'} 
print(my_set) 
2.my_set={'a', 'b', 'c'} 
for values in my_set: 
 print(values) 
  3.my_set={'a', 'b', 'c'} 
my_set.add('v') 
print(my_set)
4.my_set={'a', 'b', 'c'} 
my_set.remove('b') 
print(my_set)
5.my_set={'a', 'd', 'c'} 
my_set.discard('b') 
print(my_set) 
