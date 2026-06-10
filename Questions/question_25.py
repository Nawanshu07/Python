with open("content.txt") as f:
    data = f.read()
    data = data.replace("donkey" , "######")

print(data)

with open("content.txt" , "w") as f:
    f.write(data)