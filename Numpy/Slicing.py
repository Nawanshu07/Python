import numpy as np

array = np.array([[1 ,2 ,3 ,4],
                  [5 ,6 ,7 ,8],
                  [9 ,10 ,11 ,12],
                  [13 ,14 ,15 ,16]])

print(array[1:3])

print()

print(array[0:3,0:3])
print()

print(array[:,2])#colon to select all the rows and 2 for select columns inside that rows
print()

print(array[:, 1:3])#the first place is for rows and other one is for columns and we can independenly use indexing in both

print()
print(array[0:2 , 0:2])

print()
print(array[2: , ::-1])