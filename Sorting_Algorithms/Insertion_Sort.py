array = [1,4,7,23]

n = len(array)

for i in range(n):
    j = i
    while (j>0 and array[j-1] > array[j]):
        array[j-1],array[j] = array[j],array[j-1]
        j-=1


print(array)