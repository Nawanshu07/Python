# longest streak of consicutive numbers

numbers = [1, 2, 3, 2, 4, 5, 6, 1, 2]
count = 1
first = numbers[0]
highest = 0
for num in numbers[1:]:
    if first:
        if first+1 == num:
            count+=1
            first = num
        else:
            if highest<count:
                highest = count
            count = 1

print(count if count>highest else highest)