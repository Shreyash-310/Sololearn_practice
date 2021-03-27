"""class Queue:
    def __add__(self, contents):
        self._hiddenlist = list(contents)
    def push(self,value):
        self._hiddenlist.insert(0,value)
    def pop(self):
        return self._hiddenlist.pop(-1)
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)
queue = Queue([1,2,3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
"""

"""class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)
s = Spam()
s.print_egg()
print(s._Spam__egg)    # private  could be accessed externally with _Spam__privatemethod.
print(s.__egg)         # otherwise it will the error"""

class Pizza:
    def __init__(self,toppings):
        self.toppings = toppings
    @staticmethod                   # static method, we dont use
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("NO Pineapple!")
        else:
            return True
ing = ['cheese','onion','spam','pineapple']
if all(Pizza.validate_topping(i) for i in ing):
    pizza = Pizza(ing)