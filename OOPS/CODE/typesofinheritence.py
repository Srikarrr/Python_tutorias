#Single Inheritence A->B
class Parent:
      def func1(self):
          print("This function is in parent class.")




 class Child(parent):
       def func2("This function is in child class.")
           print("This function is in child class")


       #Drivers code
       object = Child()
       object.func1()
       object.func2()


 #multiple Inheritence A->C,B->C
 class Mother:
       mothername = ""
       def mother(self):
           print(self.mothername)

 class Father:
       fathername = ""

       def father(self):
           print(self.fathername)

 Class Son(Mother,Father):
       def parents(self):
           print("Father :",self.fathername)
           print("Mother :",self.mothername)


 #Driver's Code

       s1=Son()
       s1.fathername = "RAM"
       s1.mothername = "SITA"
       s1.parents()

#Multilevel Inheritence
# A->B->C


class GrandFather:
      def __init__(self,grandfathername):
          self.grandfathername = grandfathername

      # Intermediate class

class Father(GrandFather):
      def __init__(self,grandfathername):
          self.fathername=fathername
          #Invoking constructor of GrandFather class
          GrandFather.__init__(self,grandfathername)

      # Derived class

 class Son(Father):
       def __init__(self,sonname,fathername,grandfathername):
           self.sonname=sonname

           Father.__init__(self,fathername,grandfathername)

       def print_name(self):
           print('GrandFather name :', self.grandfathername)
           print("Father name:",self.fathername)
           print("Son Name:",self.sonname)


       #Driver code
       s1 = Son('Prince','Rampal','Lal mani')
       print(s1.grandfathername)
       s1.print_name()

 #Hierarchical Inheritence
# A->B , A->C , A->D

class Parent:
      def func1(self):
          print("This function is in parent class")

class Child1(Parent):
      def func2(self):
          print("This function is in child 2.")

class Child2(Parent):
       def func3(self):
           print("This function is in child 2.")

       #Driver's code
       object1 = Child1()
       object2 = Child2()
       object1.func1()
       object2.func2()
       object2.func1()
       object.func3()

#Hybrid Inheritence:
#Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

#F->B,F->E
#G->E
#B->A,B->C

class School:
      def func1("This Function is in school")

class Student1(School):
      def func2(self):
          print("This function is in student 1")

class Student2(School):
      def func3(School):
          print("This function is in Student 2.")

class Student3(student1,school):
      def func4(self):
          print("This Functions is in Student 3.")

object = Student3()
object.func1()
object.func2()


