import random

num = random.randint(1,101)
steps = 0

while(1):
    n = int(input("Enter your guess:"))
    steps+=1
    if(num == n):
        print(f"Congratulations you guessed right in {steps} attempts")
        break
    elif(num > n):
        print("Think a greater number!!")
    else:
        print("Think a smaller number!!")