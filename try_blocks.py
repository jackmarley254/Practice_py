# Catching specific exception
try:
    a = int(input("Please enter the first number..."))
    b = int(input("Please enter the second number..."))
    if (a < 0):
        raise TypeError
    c = a/b
    print("{} / {} = {}".format(a,b,c))
except ZeroDivisionError:
    print("Division by zero is not possible")
except ValueError:
    print("The datatypes are not proper")
except NameError:
    print("The datatypes are not defined")