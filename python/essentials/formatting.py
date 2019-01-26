x = 'seven {} {}'.format(8, 9)
print(x)

x = 'seven {1} {0}'.format(8, 9)
print(x)

x = 'seven {0:<9} {1:>9}'.format(8, 9)
print(x)

x = 'seven "{0:<9}" "{1:>9}"'.format(8, 9)
print(x)

x = 'seven "{0:<09}" "{1:>09}"'.format(8, 9)
print(x)

a = 5
b = 4
#fstring is available from 3.6
x = f'seven {a} {b}'
print(x)

x = f'seven {a:<09} {b:>09}'
print(x)

