n = int(input("enter the number: "))

for i in range(1,n):
    print(" " * (n - i),end="")
    print("*" * (i*2-1),end="")
    print()