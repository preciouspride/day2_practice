## To check for exceptions, we use try/except blocks.

#LOOK BEFORE YOU LEAP.
def division1(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

#EASIER TO ASK FOR FORGIVENESS THAN PERMISSION
def division(a, b):
    try:
        result = a / b
        print(result)
        return result
    except NameError as e:
        print(f"ValueError: {e}")
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")

try:
    division(15, 0)
except NameError:
    print("Variable a is not defined")
except ZeroDivisionError:
    print("Hey look!! I caught a Zero Division error")
except ValueError:
    print("Oh!! I caught a value error")

# l = [i for i in range(100)]
# print(l)


# for num in range(101):
#     try:
#         print(l[num])
#     except IndexError:
#         pass


# # - Exception:
#     - ArithmeticError
#         - ZeroDivisionError
#         - OverflowError
#     - LookupError
# #         - KeyError
# #         - IndexError

# dou = {"name": "Louis", "age": "30", "occupation": "soldier"}
# try:
#     dou["class"]
# except KeyError:
#     print("Key is not in dictionary")

# print("Do more in code")