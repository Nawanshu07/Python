import numpy as np

array = np.array([[1, 2, 3, 4, 5],
[6,7,8,9,10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))#standard devation
print(np.max(array))
print(np.min(array))
print(np.argmin(array))
print(np.argmax(array))
print(np.sum(array , axis=1))#row sum
print(np.sum(array , axis=0))#column sum