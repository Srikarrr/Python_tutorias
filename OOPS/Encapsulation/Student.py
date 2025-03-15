class Student:
      def __init__(self,name,rollno,age):
           self.name=name #public
           self._rollno= rollno #protected 1 underscore
           self.__age=age #private 2 underscore

      def get_age(self):
            return self.__age
      def set_age(self,age):
            if age>35:
                  print("Invalid age given.. Age should be less than 35.")   
            else:
                self.__age=age          

      def __display(self): #private method
            print(f"Hi myself {self.name} {self.__age} years old with rollno {self._rollno} from student class")     

      
      def displayPrivateData(self):
            self.__display() # from public method we can access private method

class Branch(Student):
      def show(self):
            print(f"My roll no is {self._rollno}")


s1=Student("Rahul",23,20)
print(s1._Student__age)
s1._Student__display() # name mangling object._class__propertyvariable
#s1.displayPrivateData()
#s1._Student__display()
#print(s1.__age)  # it will give error outside of class we cannot access the variable