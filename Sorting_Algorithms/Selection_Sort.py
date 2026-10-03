array = [1,4,7,23]

n = len(array)

for i in range(n):
    minimum = i
    for j in range(i + 1, n):
        if array[j] < array[minimum]:
            minimum = j
    array[i], array[minimum] = array[minimum], array[i]

print(array)  