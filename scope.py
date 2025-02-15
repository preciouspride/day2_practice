# # Variable scope => Part of your code where the variable is visible

# # Global variable

# def say_hello():
#     print(f"Hello, {variable1}")

# say_hello()

# # Local variable

variable1 = 'Kaba'

def say_hi():
    global variable1
    variable2 = "Louis"
    print(f"Hello, {variable1}")
    variable1 = "Mr, " + variable1 
    print(f"Hi, {variable2}")
    #return variable2

say_hi()
print("Done")
print("Variable1 outside the function: ", variable1)



# print(f'My variable is {variable1}')
# print(f'My variable is {variable2}')

# # say_hi()

say_hi()
print("Variable1 outside the function: ", variable1)

# i = 0
# j = 0
# for num in range(10):
#         i = num + 10
#         j = i ** 2
#         print(f'Number is {num}')
#         print(f"I is {i}")    
# print("J is:", j)