import numpy as np

# Broadcasting allows NumPy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape.

# The dimensions have the same size.
# OR
# One of the dimensions has a size of 1.

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print()

print(array1 * array2)#because one of the dimension is 1

print()
#if there are dimesntion mismatch then it will throw value error

array3 = array1 * array2
print(array3.shape)