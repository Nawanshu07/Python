import numpy as np

print("0D array: ")#also known as scaler array
array = np.array("A")
print(array.ndim)
print(array.shape)#tells the size of the array along each dimension.

print()
print("1D array: ")
array = np.array(["A", "B", "C"])
print(array.ndim)
print(array.shape)

print()
print("2D array: ")
array = np.array([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]])
print(array.ndim)
print(array.shape)

print()
print("3D array: ")
array = np.array([
	[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
	[["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
	[["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", "_"]],
])
print(array.ndim)
print(array.shape)
print()

#accesing elements
print("Accessing the elements in an multidimensional array:")
print(array[0,0,0])#multidimensional indexing
print(array[0][0][0]) #chain indexing
#both are same but upper one is short

word = array[0,0,0] + array[2,0,0] + array[2,0,0]
print(word)