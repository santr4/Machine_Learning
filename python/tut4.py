# args and kwargs revision.
# now lets make a function to take three arguments and return the sum.

def sum_three(x,y,z):
    return x+y+z

s = sum_three(2,3,4)

print(s)

# now let's say we pass more than three arguments to the sum_three function then what will happen.
# x = sum_three(2,3,4,5)
# print(x)     --> this is giving error = TypeError: sum_three() takes 3 positional arguments but 4 were given.

# **     *args --> this is to pass variable length arguments to the function 

def adder(*int):      # ** variable number of arguments can be passed on to the function as tuples.
    s = 0 
    for n in int:
        s+=n
    return s

z = adder(2,3,4,5)
x = adder(1,1,1,1,1,1,1,1)
print(z)
print(x)

# **      ** kwargs

def info(**kwargs):
    print("the type of the data is: ",type(kwargs))
    for key,value in kwargs.items():
        print("{} is {}".format(key,value))

info(firstname="aaranyak",lastname="santra",age="19",wieght="75")
    