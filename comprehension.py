### Comprehension is a shorter way to create a list from a loop
### Just like a loop, it can have conditions
### It can be done with a list, a dictionary or a tuple (generator)


## Example of a list comprehension
# print([ num for num in range(10)])

#With a conditional => Give me the list of numbers from 1 to 50 that are even numbers
l = [ num for num in range(51) if num % 2 == 0]
# print(l)

## Using comprehension, give me the square of all the even numbers from 1 to 10
squares = [ num ** 2 for num in range(1, 11) if num % 2 == 0]

# print(squares)

## Dictionary comprehension is also possible
# For example, for numbers from 1 - 10, give a dictionary of each number and it's cube
## For example {1: 1, 2: 8, 3: 27}
cube_dict = { num: num**3 for num in range(1, 11)}
print(cube_dict)