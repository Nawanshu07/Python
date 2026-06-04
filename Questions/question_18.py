def fac(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * fac(n-1)
    
n = int(input("Enter a number: "))
if (n>=0):
    print(f"The factorial of {n} is: {fac(n)}")
else:
    print("Enter a valid positive integer")