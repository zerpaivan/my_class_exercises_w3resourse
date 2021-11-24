class Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        a = self.length * self.width
        print(f"Area: {a}")


rect1 = Rectangle(10, 5)
rect1.area()
