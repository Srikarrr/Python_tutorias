from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(animal):
     def speak(self);
         print("bark")

d1 = Dog()
d1.speak()

#bark
