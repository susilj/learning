
def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f2

def f3():
    print('this is f3')

f3()

x = f1(f3)
x()

f3 = f1(f3)
f3()

#decorates the function by passing the function as parameter to the decorator function f1 
# cannot call the function f4() directly it is accessible only via the decorator function f1
@f1
def f4():
    print('this is f4')

f4()