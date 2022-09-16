
class Point:

    def move(self):
        print("move")

    def draw(self):
        print("draw")


class Point2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

class Person:
    def __init__(self,name):
        self.name = name

    def present(self):
        print(f"Hi I am {self.name}")


# ------------ Point ----------
p1 = Point();
p2 = Point();
p1.draw();
p1.x = 10
p2.x = 3
print(p1.x)
print(p2.x)
# ------------ Poin1 ----------
p3 = Point2(10,20)
print(p3.y)
# ------------ Person ----------
john = Person("John Smith")
bob = Person("Bob Smith")
john.present()
bob.present()