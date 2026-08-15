numbers = [7, 2, 15, 1, 10, 6, 17, 3, 11, 16, 5]
numbers.sort()
# [1, 2, 3, 5, 6, 7, 10, 11, 15, 16, 17]
missing = []
for i in range(len(numbers)-1):
    if numbers[i]+1 != numbers[i+1]:
        for j in (range(numbers[i]+1 , numbers[i+1])):
            missing.append(j)
         

print(missing)