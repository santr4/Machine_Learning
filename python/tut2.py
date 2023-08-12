# **    *args and **kwargs in python

# ** *args

# ** example 1:
def introduction(*argv):
    for arg in argv:
        print(arg)

introduction('Hi','my','name','is','aaranyak','santra')

# ** example 2: to illustrate *args with some extra arguments everytime.

def name(*arg):
    for x in arg:
        print("hello",x)

name('aaranyak','anupam','himanshu','gaurav','ansh','saumy','prashant','yashk','dhananjai','jishnu','srijith')

# ** **kwargs

def roommates(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key,value))

roommates(friend1='anupam',friend2='himanshu',friend3='ansh')

# ** now we will use both *args and **kwargs

def func(*args,**kwargs):
    print("args: ",args)
    print("kwargs: ",kwargs)

func('hello','aaranyak','santra',first='hello',second='himanshu',third='lath')