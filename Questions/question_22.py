f = open("file.txt" , "w")

n = int(input("Enter the number of students:"))
with open("file.txt" , "w") as f:
    f.write("Name\tclass\troll\n")
    for i in range (n):
        name = input("Enter name:")
        standard = input("Enter class:")
        roll = input("Enter roll number:")
        f.write(f"{name}\t{standard}\t{roll}")
