#program to open some file , and if that file is not existing then generate a message 

try:
    with open("filee.txt" , "r") as f:
        print(f.read())
        
except FileNotFoundError as e:
    print("File not found")
    