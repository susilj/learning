
def main():
    kitten(5, 6)
    kitten(5, 6, 7)
    a = [3]
    mutableFunction(a)
    print(f'a in main is {a}')
#arguments with default values must be at the end of parameter list
def kitten(a, b, c = 0):
    print(a, b, c)

def mutableFunction(a):
    a[0] = 5
    print(a)

if __name__ == '__main__': main()