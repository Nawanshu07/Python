import numpy as np

rng = np.random.default_rng()

#we can also use seed to reproduce same value , otehrwise numpy will use some seed for us

print(rng.integers(1,11,4))
print()

print(np.random.uniform(low = -1 , high = 1))#keyword arguments
print()

print(rng.integers(1,11,(3,2)))
print()

array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)
print()

fruits = np.array(["Apple" , "Orange" , "Banana" , "Kela"])
fruit = rng.choice(fruits , size = (2,2))
print(fruit)