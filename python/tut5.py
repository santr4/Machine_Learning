# ** oops in python - classes and objects

class Person:
    name = "surya"
    age = 8
    salary = 100000

a = Person()
a.name = "aaranyak santra"
a.age = 20
a.salary = 10000000
print(a.name)
print(a.age)
print(a.salary)

b = Person()
print(b.name)   # a and b are the objects of the class Person.

# *! self ka matlab vo object jiske liye ye method call kia ja raha hai

class startup:
    ceo = "ankush"
    name = "cisco"
    employees_no = 1000
    funding = 500
    office = 5
    def info(self):
        print(f"{self.ceo} is the ceo of the company: {self.name}")

a = startup()
a.ceo = "aaranyak"
a.name = "AImankind"
a.info()

b = startup()
b.ceo = "shreya"
b.name = "AIunleash"
b.info()