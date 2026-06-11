n = int(input("Enter the limit: "))

def gen_table(n):
    table = ""
    for i in range (1,11):
        table+= f"{n} x {i} = {n*i}\n"
    
    with open(f"table/table_{n}.txt" , "w") as f:
        f.write(table)

for i in range (1,n+1):
    gen_table(i)
            