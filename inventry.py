##Parameter is the name that you pass to the function at the time when you are defining the function. The parameter name can be anything. But is should be a meaningful name
## Argument is the name you pass to the function at the time when you are calling/using the function. It must be an item/variable that is DEFINED in the program

store = {
    "milk": 8.99,
    "sugar": 2.50,
    "cheese": 4.75,
    "salt": 6.90,
    "eggs": 28.50
}

store.values()

#1: Write a function that takes a dictionary as parameter, and returns the total of the prices
#2: Write a function that will take a list of items, and if the items are in the dictionary, return the sum of their prices
#3: Write a function that will add items into our store. It should take the name of the item and the price

def total_price(store_dictionary):
    total = 0
    for price in store_dictionary.values():
        total += price
    return total

print(total_price(store))


def total_store_price(my_store):
    store_prices = my_store.values()
    total = sum(store_prices)
    return total

def total_price_of_items(items, store_dict):
    total = 0
    for item in items:
        if item in store_dict:
            total += store_dict[item]
    return total

def total_price_items(items, store_dict):
    sum(store_dict[item] for item in items if item in store_dict)

print(total_price_of_items(["milk", "eggs"], store))
print(total_price_of_items(["salt", "eggs", "watermelon"], store))

def add_item(item, price, store_dict):
    store_dict[item] = price
    return store_dict

print(add_item("orange", 5.99, store))