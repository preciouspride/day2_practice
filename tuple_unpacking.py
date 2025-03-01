t = (1, 2, 3, 4)


zero, one, two, three = t

print(f'{zero}, {one}, {two}, {three}')

a = 10
b = 20

print(f'a={a}. b={b}')

a, b = b, a

print(f'a={a}. b={b}')

temp = a
a = b
a = temp