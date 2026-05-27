#Program to print greatest of 4 number entered by the user 
largest = int(input("Enter the number: "))

for i in range (3):
    a = int(input("Enter the number: "))

    if(largest < a):
        largest = a

print("Largest : ",largest)