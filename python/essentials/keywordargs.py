

def main():
    kitten(Buffy = 'meow', Zilla = 'grrr', Angel = 'rawr')
    x = dict(Buffy = 'meow', Zilla = 'grrr', Angel = 'rawr')
    kitten(**x) 

def kitten(**kwargs):
    if len(kwargs):
        for kwarg in kwargs:
            print('kitten {} says {}'.format(kwarg, kwargs[kwarg]))
    else: print('Meow!!!')
        
if __name__ == '__main__': main()