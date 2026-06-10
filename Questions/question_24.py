#Stone paper scisors game 
import random


score = 0
while(1):
    computer = random.choice([1,-1,0])
    inp = input("Enter your choice , stone paper or scissors:")
    dic = {"s":1 , "p":0 , "sc":-1}

    if inp not in dic:
        print("Invalid choice!")
        continue

    me = dic[inp]

    dic2 = {1:"Stone" , 0:"paper" , -1:"scissors"}

    print(f"You choose {dic2[me]} and computer chose {dic2[computer]}")

    if(computer == me):
        print("Draw")

    else:

        if(computer == 1 and me == 0):
            print("You Win")
            score+=5
        elif(computer == 1 and me == -1):
            print("You lose")
            break
        elif(computer == 0 and me == 1):
            print("You lose")
            break
        elif(computer == 0 and me == -1):
            print("You Win")
            score+=5
        elif(computer == -1 and me == 1):
            print("You Win")
            score+=5
        elif(computer == -1 and me == 0):
            print("You lose")
            break
        else:
            print("Something went wrong")

with open("high_score.txt" , "r") as f:
    data = f.read().strip()

    if (data == ""):
        hscore = 0
    else:
        hscore = int(data) 
    
if score > hscore:
    with open("high_score.txt", "w") as f:
        f.write(str(score))
    print("You beat the high score!!")