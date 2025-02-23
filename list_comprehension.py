even_numbers = []
for num in range(10_000_000_000):
    if num % 2 == 0:
        even_numbers.append(num ** 2)

print(even_numbers)