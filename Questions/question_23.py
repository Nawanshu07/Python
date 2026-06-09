elem = input("Enter the element you want to search:")
found = 0
with open("file.txt" , "r") as f:
    if elem in f.read():
        found +=1

print(found)