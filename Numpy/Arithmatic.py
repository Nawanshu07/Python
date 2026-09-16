import numpy as np

array = np.array([1 ,2,3,4,5])

# scaler arithmatic
print(array + 2)
print()

print(array * 2)
print()

print(array / 2)
print()

print(array ** 2)
print()

#Vectorised math fucntions

array = np.array([2.2,4.0,8.4])

print(np.sqrt(array))
print()

print(np.round(array))
print()

print(np.pi)
print()

radius = np.array([2,4,6])
print(np.round(np.pi * radius ** 2))
print()

#Element-wise arithmatic

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2) 
print()

print(array1 * array2)   
print()

print(array1 / array2)
print()

print(array1 ** array2)
print()

#Comparison Operators
score = np.array([100 ,40 , 60 , 33 ,54 , 32])

print(score > 60)
print()

print(score < 33)
print()

score[score < 33] = 0
print()

print(score)
