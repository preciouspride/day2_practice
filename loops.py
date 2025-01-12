# 2 Types of Loops:

positive_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(len(positive_numbers))

##  DETERMINISTIC VS NON-DETERMINISTIC

class_participants = ['Kaba', 'Kelly', 'Louis', 'Mofor']

# for loop vs while
#ITERATE / ITERATION / ITERABLES

# for item in a container:
    # code block
    # code block
    # code block
    # code block
    # code block
#code => NOT PART OF LOOP

# index  => postion of an element in a sequence

# for num in positive_numbers:
#     print(num)
# print("Done")

# for member in class_participants:
#     print(member)
# print("Done")

# for i in range(1, 10, 3):
#     print(i)
# print('Done')

# for i in range(len(positive_numbers)):
#     print(positive_numbers[i])

# % => Modulo: Returns the remainder when you divide E.g 7 % 5 = 2
# x % 2 = 0: Even numbers always return 0 when divided 2

# For each number, print beside the number if the number is even or odd
# For example
# 1: "Odd"
# 2: "Even"
# 3: "Odd":
# 4: "Even"
for num in positive_numbers:
    print(num)