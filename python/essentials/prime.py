def isPrime(n):
    if n <= 1:
        return False;
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def list_primenumbers():
    for n in range(100):
        if isPrime(n):
            print(n, end = ' ', flush = True)
    print()

n = 5

if isPrime(n):
    print('{} is prime number'.format(n))
else:
    print('{} is not prime number'.format(n))

list_primenumbers()