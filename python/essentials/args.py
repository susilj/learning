

def main():
    kitten('meow', 'grrr', 'cry', 'cute face')
    x = ('meow', 'grrr', 'cry')
    kitten(*x)

def kitten(*args):
    if len(args):
        for arg in args:
            print(arg)
    else: print('Meow!!!')
        
if __name__ == '__main__': main()