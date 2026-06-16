class book:
    pages = 0
    def __init__(self , pg):
        self.pages = pg

    def __add__(self, other):
        return self.pages + other.pages
    
b1 = book(150)
b2 = book(250)

b3 = b1 + b2

print(b3)