n = int(input("Enter the limit: "))

for i in range (1 , n+1):
    for j in range (1,10):
        with open("file.txt" , "w") as f:
            f.write(f"{i} x {j} = {i*j}")
            