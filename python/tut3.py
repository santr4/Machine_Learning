# ** decorators -- this are actually functions which modifies another function

def greet(fx):
    def mfx(*args, **kwargs):
        print("hello!")
        fx(*args, **kwargs)
        print("thankyou for using the function")
        print()
    return mfx

@greet   # // decorator
def fun():
    print("aaranyak santra")

fun()

@greet   # // decorator
def add(a,b):
    print(a+b)

add(1,2)