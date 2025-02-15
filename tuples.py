## Collection / Sequence
## Ordered
## Immutable
## Heterogenous / Homogenous
## Tuples are iterable

fruits_tuple = ("Mango", "Orange", "Banana", "Apple")

# for item in fruits_tuple:
#     print(item)


# empty_tuple = tuple()
# print(empty_tuple)

# print(fruits_tuple[0])


# mango = fruits_tuple[0]
# orange = fruits_tuple[1]
# banana = fruits_tuple[2]
# apple = fruits_tuple[3]

## Tuple destructuring
elt1, elt2, elt3, elt4 = fruits_tuple

print(elt1)


def add(a, b, c):
    return a + b + c

print(add(5, 7, 9))

def sum_and_prod(a, b):
    sum_ = a + b
    prd = a * b
    return sum_, prd
va1, va2 = sum_and_prod(5, 10)

print(va1, va2)

numbers = (1, 2, 3, 4, 5, 6, 7, 8)


print(numbers[10])