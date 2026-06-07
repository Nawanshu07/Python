def sum(a):
    if(a == 1):
        return 1
    else:
        return a + sum(a-1)
    
a = sum(10)
print(a)

