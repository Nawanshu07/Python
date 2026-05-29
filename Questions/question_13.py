num = int(input("Enter the number: "))

isprime = 1

for i in range (2,num):
    if(num % i == 0):
        isprime = 0
        break

if(isprime == 1):
    print("Number is a prime number")
else:
    print("Number is not a prime number")