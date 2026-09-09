# Calculate Perimeters Using Different Shapes Object

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        # Write your code here
        return (self.length + self.breadth) * 2


class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        # Write your code here
        return self.side * 4


length = int(input())
breadth = int(input())
side = int(input())

shapes = [Rectangle(length, breadth), Square(side)]

for shape in shapes:
    print(shape.perimeter())