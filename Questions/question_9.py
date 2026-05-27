# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at leaặt 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
c = int(input("Enter marks of subject 3: "))

total_percentage = (a + b + c) / 300 * 100

if(a >= 33 and b >= 33 and c >= 33 and total_percentage >= 40):
    print("You are passed")
else:
    print("You are failed")