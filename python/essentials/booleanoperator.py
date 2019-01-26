#and
a = True
b = False

if a and b:
    print('a and b are true')
else:
    print('a and b are not true')

if a or b:
    print('a or b is true')
else:
    print('a or b is not true')

if not a:
    print(f'{a} is true')
else:
    print(f'a = {a} is false (negated)')

c = ('bear', 'tiger', 'cat', 'dog')
d = 'dog'

if d in c:
    print('dog is available in the list')
else:
   print('dog is not available in the list')

if d in c[3]:
    print('dog is available as fourth element in the list')
else:
   print('dog is not available as fourth element in the list') 