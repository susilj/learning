x = [1, 2, 3, 4, 5]

for i in x:
    print(i, end = ' ', flush = True)

print()

x[2] = 54
for i in x:
    print(i, end = ' ', flush = True)

#Tuple elements within "()" is similar to list only it cannot be modified immutable
print()
x = (1, 2, 3, 4, 5)

for i in x:
    print(i, end = ' ', flush = True)

print()

# x[2] = 54
# for i in x:
#     print(i, end = ' ', flush = True)

#range is also immutable and can be modified wrapping it inside list
# x = list(range(5))
# x[2] = 22

for i in range(5):
    print(i, end = ' ', flush = True)

print()
for i in range(5, 50):
    print(i, end = ' ', flush = True)

print()
for i in range(5, 50, 5):
    print(i, end = ' ', flush = True)

print('Dictionary')

x = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
for k in x:
    print('key is {}'.format(k))

for k, v in x.items():
    print('key: {0}, value: {1}'.format(k, v))
