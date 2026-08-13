n = int(input("Enter the n:"))
num = n-1
for i in range(n):
    for j in range (n-i):
        print(" ",end="")

    for k in range (i*2-1):
        print("*" , end="")

    print()

for i in range(2,n):
    for k in range(i):
        print(" ", end="")

    for k in range((n-i)*2-1):
        print("*", end="")

    print()
    
for i in range(n):
    for j in range (n-i):
        print(" ",end="")

    for k in range (i*2-1):
        print("*" , end="")

    print()

for i in range(2,n):
    for k in range(i):
        print(" ", end="")

    for k in range((n-i)*2-1):
        print("*", end="")

    print()
    