numbers = [4, 7, 2, 4, 9, 7, 1, 2, 7, 5]
duplicates = []
for i in range(len(numbers)):
    dup = False
    for j in range(1,len(numbers)):
        if (numbers[i] == numbers[j] and i!=j and numbers[i] not in duplicates):
            dup = True
            break
    if dup:
        duplicates.append(numbers[i])

print(duplicates)