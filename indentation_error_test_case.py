# try:
#     print("Welcome to PYnative")
#         print("Learn Python with us..")
# except IndentationError:
#     print("indentaion error offured`")


try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a/b
    print("The answer of a divide by b:", c)
except ValueError:
    print("Entered value is wrong")
except ZeroDivisionError:
    print("Can't divide by zero")
