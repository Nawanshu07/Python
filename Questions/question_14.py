n = (int(input("Enter the value of n: ")))

for i in range (2,n):
    isprime = 1
    for j in range (2,i):
        if(i % j == 0):
            isprime = 0
            break
    if(isprime):
        print(i)
