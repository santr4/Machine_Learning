# ** constructors in python.
# we all know that whenever I make an object for the class then the constructor of that class is automatically initiated.

class company:

    def __init__(self):
        print("Ram and Sita are good friends.")

a = company()
b = company()



class person:
    def __init__(self,name,nature):
        self.name = name
        self.nature = nature
    def info1(self):
        print(f"{self.name} is a {self.nature} boy.")
    
    def info2(self):
        print(f"{self.name} is a {self.nature} girl.")

a = person("aaranyak","good")
a.info1()
b = person("nehal","good")
b.info2()
