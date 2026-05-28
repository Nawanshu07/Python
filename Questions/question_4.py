a = 0
b = 1
n = int(input("Enter the limit of series:"))

for i in range (n):
    print(a , end=" ")
    a , b = b , a+b