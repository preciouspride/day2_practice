from math import sqrt, pi, factorial
from functions import convert_celcius_to_fahrenheit as cctf
import functions as fxn


num = 10000

sqrt_num = sqrt(num)
print(sqrt_num)

radius = 15
# pi * radius squared

area = pi * (radius ** 2)
print(area)

temp_in_abj = cctf(35)
print(temp_in_abj)


fact = factorial(10)
print(fact)