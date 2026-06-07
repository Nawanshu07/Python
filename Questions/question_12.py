n = int(input("enter the number: "))

for i in range(1,n):
    print(" " * (n - i),end="")
    print("*" * (i),end="")
    print()