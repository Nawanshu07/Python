n = int(input("Enter a number: "))

table = [i*n for i in range(1,11)]

with open("multiplication-table.txt" , "a") as file:
    file.write(str(table) + "\n")
