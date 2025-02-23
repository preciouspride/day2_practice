even_numbers = (num for num in range(10_000_000_000) if num % 2 == 0)


for num in even_numbers:
    print(num, end=" ")
    if num > 100:
        break


print("\n")

for num in even_numbers:
    print(num, end=" ")
    if num > 200:
        break