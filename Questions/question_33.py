try:
    a = int(input("Enter a number:"))
    b  = int(input("Enter a number:"))
    c = a/b
except ZeroDivisionError as z:
   print("Division by zero is not possible ")
except ValueError as v:
   print("Please enter valid values")