class Rectangle:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if (type(x) == 'integer' and type(y) == 'integer'):
            print("correct")
        else:
            print("wrong")

    def area(self):
        return self.y * self.x

    # use __str__ method to return string representation to the end user
    def __str__(self):
        return "rectange " + str(self.x) + " " + str(self.y)


#     use __repr__ method to return output to the dev
#     def __repr__(self):
#         return str(self.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("hello my name is", self.name)

    def my_age(self):
        print("my age is", self.age)


class TenYearOld(Person):
    def __str__(self):
        return str(self.age)

class TenYearOldSelf(Person):
    # create a new constructor that is different from the Parents inherited constructor
    def __init__(self, name):
        # call the parent's constructor method and modifies it
        Person.__init__(self, name, 10)

#     Overwrite an inherited method
    def greet(self):
        print("my name is", self.name, " and my age is", self.age)



print(type(8.3))
r = Rectangle(2, 4)
print(r.area())
print(r)

c = TenYearOld('ron', 14)
c.my_age()

d =TenYearOldSelf('slater')
d.greet()