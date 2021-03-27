"""class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
    def bark(self):
        print("woof!")
felix = Cat("ginger",4)
print(felix.color)
felix.bark()
"""
"""class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
class cat(Animal):
    def purr(self):
        print("purr!")
class Dog(Animal):
    def bark(self):
        print("woof!")
fido = Dog("Fido",'brown')
print(fido.color)
fido.bark()"""

# Inheritence
"""class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)

B().method()"""

class A:
    def method(self):
        print("A method")
class B(A):
    def another_method(self):
        print("B method")
class C(B):
    def third_method(self):
        print("C method")
class D(A):                     # for another example of inheritence
    def spam(self):
        print(2)
        super().method()
c = C()
c.method()
c.another_method()
c.third_method()
D().spam()