
x = 8
y = 8

if x < y:
  print('x < y: x is {} and y is {}'.format(x, y))
elif x > y: print('x > y: x is {} and y is {}'.format(x, y)) #also works for single line and not for blocks (multiline)
else: print('Unable to determine')

x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)

print('x id is {}'.format(id(x)))
print('y id is {}'.format(id(y)))

print('x[0] id is {}'.format(id(x[0])))
print('y[0] id is {}'.format(id(y[0])))

if(x[0] is y[0]):
  print('elements are same')
else:
  print('elements are different')

if(x is y):
  print('x is same as y')
else:
  print('x is not same as y')

y = list(y)
if isinstance(x, tuple):
  print('x is tuple')
if isinstance(y, list):
  print('y is list')