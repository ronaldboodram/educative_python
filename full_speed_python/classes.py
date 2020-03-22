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


print(type(8.3))
r = Rectangle(2, 4)
print(r.area())
print(r)
