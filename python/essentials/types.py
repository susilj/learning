x = 7
print('x is {}'.format(x))
print(type(x))

x = 7.0
print('x is {}'.format(x))
print(type(x))

x = 7 * 3
print('x is {}'.format(x))
print(type(x))

x = 7 * 3.14159
print('x is {}'.format(x))
print(type(x))

x = 7 / 3
print('x is {}'.format(x))
print(type(x))

x = 7 // 3
print('x is {}'.format(x))
print(type(x))

x = 7 % 3
print('x is {}'.format(x))
print(type(x))

x = .1 + .1 + .1 - .3
print('x is {}'.format(x))
print(type(x))

from decimal import *
a = Decimal('.01')
b = Decimal('.03')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))

x = '7'
print('x is {}'.format(x))
print(type(x))

x = "7"
print('x is {}'.format(x))
print(type(x))

x = '''

7

'''
print('x is {}'.format(x))
print(type(x))

x = """
7
"""
print('x is {}'.format(x))
print(type(x))

x = True
print('x is {}'.format(x))
print(type(x))

x = None
print('x is {}'.format(x))
print(type(x))

x = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x))
print('type of second element is {}'.format(type(x[1])))