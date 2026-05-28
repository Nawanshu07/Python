#write a program to inpute 8 numbers and display unique ones at once

a = 0
s = set()
for i in range (8):
    a = int(input("Enter number:"))
    s.add(a)

print(s)