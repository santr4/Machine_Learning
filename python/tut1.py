# ** higher order functions

# ** a higer order function is that function which takes another fucntion as a parameter or returns a function as a result

# example 1:

def shout(text):
    return text.upper()

print(shout('hello'))

yell = shout

print(yell('hello\n'))


# now we will take another good example to get clear in higher order functions.

def shout(text):
    return text.upper()

def whispher(text):
    return text.lower()

def greet(func):

    greeting = func("Hello, I am Aaranyak Santra. Nice to meet you!")
    print(greeting)

greet(shout)

greet(whispher)