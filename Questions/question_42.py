#missing number in consicutive series 

numbers = [1, 2, 3, 5, 6,7]
number = 0
first = numbers[0]

for num in numbers[1:]:
    if first+1 != num:
        number = first
    else:
        first = num

if number == 0 :
    number = numbers[len(numbers)-1]

print(number+1 if number else "")