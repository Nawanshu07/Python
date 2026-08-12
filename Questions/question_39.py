# Program to find duplicate and first occurance of non duplicate number

numbers = [4, 7, 2, 7, 9, 4, 2, 7, 5]

for i in range(len(numbers)):
    duplicate = False
    for j in range(len(numbers)):
        if(numbers[i] == numbers[j]):
            if(i != j):
                duplicate = True
                break
    if not duplicate:
        print(numbers[i])
        break

