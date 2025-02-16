## Collection
## iterable
## NOT Sequence => NOT ORDERED => DOES NOT HAVE INDEX
## KEY/VALUE PAIR

empty_dict = {}
empty_dict2 = dict()

person = {"name": "Kaba", "age": 25}

# print(person)
# print(person["name"])

print(person["age"])

# print(person)

person["location"] = "Abidjan"
print(person)

for k, v in person.items():
    print((k, v))

#Dictionary methods
# keys() => Prints out the keys in the dictionary
# values() => Prints out the values in the dictionary
# items()

# print(person.items())