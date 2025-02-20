#Python Numbers
"""
Three numeric types in python
1.int
2.float
3.complex
"""

#int
x = 1
y = 23454345
z = -3242
print(type(x),type(y),type(z))

#float
x = 1.0
y = 1.10
z = -32.4
print(type(x),type(y),type(z))

"""
Float can also be scientific numbers with an "e" to indicate the power of 10.
"""

x = 23e2
y = 12E3
z = -30.9e100
print(type(x),type(y),type(z))

#Complex
x = 3+5J
y = 5j
z = -5j
print(type(x),type(y),type(z))

#Type conversion
x = 1 
y = 2.3

a = float(x)
b = complex(y)

print(a, b)

#Random Number
"""
Python does not have a random() function to make a random number, but python has a built-in module called random that can be used to make random numbers
"""

import random

print(random.randrange(1, 10))