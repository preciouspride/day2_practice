#### Name block of code 

## Reusable => Functions make you code to be reusable
## Readable and Organized
## Managing code is easier

## Example
## Formula: (celsius * 9/5.4) + 32
## 34 => (34 * 9/5.4) + 32 => 93.?/

# print("Hello. Welcome to our Python class for today")
# print("I hope we are going to learn many useful things today")
# print("Start up your computer and get ready")
# print("Start your vscode and follow along with everything I type")


#### Format for defining a function
## def => key word that defines a function
## name => name of the function followed by brackets ()
## If there are any arguments, put them in the brackets
## : => Colon to indicate the start of the function body
## return => The function will return the value after the return keyword

## Function is always going to return a value

# def welcome_students():
#     print("Hello. Welcome to our Python class for today")
#     print("I hope we are going to learn many useful things today")
#     print("Start up your computer and get ready")
#     print("Start your vscode and follow along with everything I type")

# welcome_students()



# #Function with paramters:
# def welcome_students(name, subject):
#     print(f"Hello {name}. Welcome to our {subject} for today")
#     print("I hope we are going to learn many useful things today")
#     print(f"{name}, Start up your computer and get ready")
#     print("Start your vscode and follow along with everything I type")

# welcome_students("Mofor", "Statistics Class")

# ## Function with a return value
# def full_name(first_name, last_name):
#     first_name = first_name.capitalize()
#     last_name = last_name.capitalize()
#     print(f'First name is {first_name}')
#     print(f'Last name is {last_name}')
#     return f'{last_name}, {first_name}'

# names = full_name("louis", "fru")

# print(names)

# def add(a, b):
#     print(f'Adding the numbers {a} and {b}')
#     return a + b

# answer = add(2, 5)
# print(answer)

## Fahrenheit => (celsius * 9/5) + 32

def convert_celcius_to_fahrenheit(celcius):
    value_in_fah = (celcius * 9/5 ) + 32
    return value_in_fah
temp_in_abidjan_in_Fah = convert_celcius_to_fahrenheit(32)
print(temp_in_abidjan_in_Fah)

### ASSIGNMENT ####

# 1. Create three functions that mimick subtraction, multiplication and division +> All take two parameters
# 2. Create a function that takes a number and returns the square of the number => Take one parameter
# 3. Create a function that takes a number, and checks if the number is even or odd. If the number is even, return 1. If the number is odd, return 0

## Bonus Assignment:
# Create a function that takes three numbers, and returns the number with the highest ABSOLUTE value