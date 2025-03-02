# d = {
#     "name",
#     "age",
#     "location",
#     "profession",
#     "dob",
#     "name"
# }

# d.add("hobby")
# d.remove("dob")

# print(d)
# print("\n")
# print(type(d))

# s = set("mississippi")
# print(s)

# l = list(s)
# print(l)

# s1 = {'a', 'b', 'c'}

# s2 = {True, False}

# s3 = {'a', 100, 200}

# print(s2.isdisjoint(s3))

# d = {
#     "name",
#     "age",
#     "location",
#     "profession",
#     "dob",
# }

# try:
#     d.remove("hobby")
# except KeyError as ex:
#     print("Key does not exist", ex)
# print(d)

# d.discard("hobby")
# print(d)

s1 = set(range(10))
s2 = set(range(10, 15))
s3 = set(range(5, 12))
s4 = set(range(3, 7))
s5 = set(range(3, 7))
print(s1)
print(s2)
print(s3)
print(s4)

print("\n")

#<=/>= checks for subsets/supersets respectively
# print(s1 > s5)

# | produces the union of two sets 
# & produces the intersection of two sets

# print(s1 & s3)

# print(s1 | s3)

# Create list of items sold from our store
items_sold = [
    "milk",
    "cheese",
    "sugar",
    "salt",
    "eggs",
    "eggs"]

# Create a list of items returned from our sold inventory
returned_items = [
    "milk",
    "salt",
    "salt",
    "eggs"]