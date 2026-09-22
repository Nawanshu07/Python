def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal  x
        print(x)
    myfunc2()
    

x = 10
myfunc1()