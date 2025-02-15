## List = Data structure: Holds data
## Data is ordered => position 1, 2, 3, etc
## Data is mutable => Remove items from the list. Add items to the list
## Data is heterogenous => Holds different types of data
## Lists are iterable

fruits_list = ["Mango", "Orange", "Banana", "Apple"]

numbers = [10, 20, 30, 40, 50]

print(fruits_list[1])

fruits_list.append("Guava")
print(fruits_list)

fruits_list.insert(0, "Lemon")
print(fruits_list)

# print("Removing last element:", fruits_list.pop())
# print(fruits_list)


# empty_list = [] #Using a LITERAL to create a list
# empty_list = list()

print(len(fruits_list))
# print(fruits_list[10])

fruits_list[0] = "Pear"

print(fruits_list)

test_fruit = []
test_fruit[0] = "Papaw"
print(test_fruit)