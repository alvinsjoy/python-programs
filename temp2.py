from abc import ABC, abstractmethod
class myClass(ABC):
    def myMethod(self):
        pass

obj = myClass()
obj.myMethod()

class newClass(myClass):
    def newMethod(self):
        print("Implementation of newMethod")

obj = newClass()
obj.newMethod()

