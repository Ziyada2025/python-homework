1.
my_list=[12.23, 13.32, 100, 36.32] 
print(my_list)
import numpy as np 
numpy_array=np.array(my_list) 
print(numpy_array) 
2. 
import numpy as np  
my_array=np.array([2,3,4,5,6,7,8,9,10]) 
matrix=my_array.reshape(3,3) 
print(matrix)
3. 
import numpy as np  
null_vector=np.zeros(10) 
print(null_vector) 
null_vector[5]=11 
print(null_vector) 
4. 
import numpy as np  
array=np.arange(12,38) 
print(array) 
5. 
berilgan=[1, 2, 3, 4] 
import numpy as np  
my_float=np.array(berilgan, dtype=float)
print(type(my_float)) 
6. 
import numpy as np

def temperature_conversions():
  
    fahrenheit_input = np.array([0, 12, 45.21, 34, 99.91])
    celsius_input = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
    
    print("=== Temperature Conversions ===\n")
    
    print("Values in Fahrenheit degrees:", fahrenheit_input)
    f_to_c = (fahrenheit_input - 32) * 5/9
    print("Values in Centigrade degrees:", np.round(f_to_c, 2))
    
    print()
    print("Values in Centigrade degrees:", celsius_input)
    c_to_f = (celsius_input * 9/5) + 32
    print("Values in Fahrenheit degrees:", np.round(c_to_f, 2))
temperature_conversions() 
7. 
my_array=[10, 20, 30] 
import numpy as np
aa=np.append(my_array, [40,50,60,70,80,90]) 
aa 
8. 
from numpy import random 
x=random.randint(100,size=10) 
mean_value = np.mean(x)
median_value = np.median(x)
std_value = np.std(x) 
print(f'random numbers is: {x} and mean_value: {mean_value},median_value :{median_value }, std_value :{std_value }') 
9. 
import numpy as np
random_array = np.random.uniform(1, 10, (10, 10))

print("10x10 Random Array (values between 1 and 10):")
print(random_array)
print("\n" + "="*50)

min_value = np.min(random_array)
max_value = np.max(random_array)

print(f"\nMinimum value: {min_value:.6f}")
print(f"Maximum value: {max_value:.6f}")
print(f"Range: {min_value:.6f} to {max_value:.6f}") 
10. 
import numpy as np
random_3d_array = np.random.uniform(1, 10, (3, 3))
print(f"3x3x3 Random Array: {random_3d_array}")
