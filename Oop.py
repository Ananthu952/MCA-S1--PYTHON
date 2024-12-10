class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def display(self):
        print(f"Area of the rectangle is {self.area()}")
        print(f"Perimeter of the rectangle is {self.perimeter()}")
    def compare_area(self,other):
        if self.area()==other.area():
            print("Rectangle are equal")
        elif self.area()>other.area():
            print("Rectanlge 1 is greater than rectangle 2")
        else:
            print("Rectangle 2 is greater than rectangle 1")
print("Enter the dimentions of the first rectangle")
l=int(input("Enter the length of the rectangle "))
b=int(input("Enter the breadth of the rectangle "))
rect1=rectangle(l,b)
rect1.display()
print("Enter the dimentions of the second rectangle")
l2=int(input("Enter the length of the rectangle "))
b2=int(input("Enter the breadth of the rectangle "))
rect2=rectangle(l2,b2)
rect2.display()
rect1.compare_area(rect2)