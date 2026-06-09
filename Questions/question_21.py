#Stone paper scisors game 
import random


computer = random.choice([1,-1,0])
inp = input("Enter your choice , stone paper or scissors:")
dic = {"st":1 , "pa":0 , "sc":-1}
me = dic[inp]
dic2 = {1:"Stone" , 0:"paper" , -1:"scissors"}


print(f"You choose {dic2[me]} and computer chose {dic2[computer]}")
if(computer == me):
    print("Draw")
else:
    if(computer == 1 and me == 0):
        print("You Win")
    elif(computer == 1 and me == -1):
        print("You lose")
    elif(computer == 0 and me == 1):
        print("You lose")
    elif(computer == 0 and me == -1):
        print("You Win")
    elif(computer == -1 and me == 1):
        print("You Win")
    elif(computer == -1 and me == 0):
        print("You lose")
    else:
        print("Something went wrong")