class calculator:
    def square(self , num):
        print(f"The square of {num} is {num * num} ")
                                                                                                    
    def cube(self , num):
        print(f"The cube of {num} is {num * num * num} ")

    def sqrt(self , num):
        print(f"The square root of {num} is {num ** 1/2} ")

n = calculator()
n.square(5)