#BREAK AND CONTINUE

#BREAK:

positive_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in positive_numbers:
    if num % 2 == 0:
        num + 100
    else:
        continue
    print(f'{num} is even')
    # More lines of code


for num in positive_numbers:
    if num % 2 == 0:
        print('{num} is Even')
        break

print(len(positive_numbers))