
class Shape():
    def circle_Area(self, r):
        return 3.14 * (pow(r, 2))

    def circle_circumference(self, r):
        return 2 * (3.14 * r)

    def rectangle_Area(self, l, w):
        return l * w

    def rectangle_Perimeter(self, l, w):
        return 2 * (l * w)


class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return super().circle_Area(self.radius)

    def diameter(self):
        return super().circle_circumference(self.radius)


class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return super().rectangle_Area(self.length, self.width)

    def perimeter(self):
        return super().rectangle_Perimeter(self.length, self.width)


print("For Rectangle type: 1 \n for Circle type: 2")
mode = int(input())
if mode == 1:
    x = int(input("Enter the LENGTH of rectangle"))
    y = int(input("Enter the WIDTH of rectangle"))
    rect = Rectangle(x, y)
    print("The area of rectangle is :", rect.area())
    print("The perimeter of rectangle is: ", rect.perimeter())

elif mode == 2:
    r = int(input("Enter the RADIUS of circle"))
    circ = Circle(r)
    print("The Area of Circle is : ", circ.area())
    print("The Circumference of circle is: ", circ.diameter())

else:
    print("Error")
