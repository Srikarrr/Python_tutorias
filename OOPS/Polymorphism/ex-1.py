def sum(a,b):
    print(a+b)

sum(2,3)
def sum(a,b,c): #overrided
    print(a+b+c)

sum(2,3,4)
sum(3,4)          

#Method over loading

class user:
     
         def __init__(self,name,mobileNumber,address=""):
             if(address==""):
                  self.C1(name,mobileNumber)
             else:
                  self.C2(name,mobileNumber,address)

         def C1(self,name,mobileNumber):
              self.name=name
              self.mobileNumber=mobileNumber   

         def C2(self,name,mobileNumber,address):
              self.name=name
              self.mobileNumber=mobileNumber
              self.address=address 
                         
 
u1 = user("Mayank","9999999","Delhi")

#Method Overriding

#sub class or child class to provide a specific implementation of a method that is already provided 
# by one of its superclass or parent class

class Animal:
     def sound(self):
          return 'Some Sound'
     
class Dog(Animal):
     def sound(self):
          return 'Bark'

obj = Dog()
print(obj.sound())  
#o/p Bark

obj = Animal()
print(obj.sound())
#o/p some sound

#Operator overloading
        
class Grandparent:
    def __init__(self):
         print('GrandParent Constructor')

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print('Parent Constructor')

class Child(Parent):
     def __init__(self):
        super().__init__()
        print('Child Constructor') 

obj = Child()

#O/P
#GrandParent Constructor
#Parent Constructor
#Child Constructor

#Diamond problem

class A:
     def show(self):
          return 'A'
     
class B(A):
     def show(self):
          return 'B'
     
class C(A):
     def show(self):
          return 'C'

class D(B,C):
     pass

obj = D()
print(obj.show())          

#O/P B

#Complex code

class A:
     def __init__(self):
          self.value = 'A'

class B(A):
     def __init__(self):
          super().__init__()
          self.value = 'B'


class C(A):
     def __init__(self):
          super().__init__()
          self.value= 'C'

class D(B,C):
     def __init__(self):
          super().__init__()

obj = D()
print(obj.value)

#O/P





                         