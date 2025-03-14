#Single Inheritence
class Grandfather:
      def __init__(self,name,age):
          self.name = name
          self.age  = age

      def show_details(self):
            return f'Name: {self.name}, Age: {self.age}'

      def speak(self):
          return "Grandfather speaks wisely."

class Father(Grandfather):
      def __init__(self,name,age,occupation):
          super().__init__(name,age)
          self.occupation = occupation

      def showOccupation(self):
        print(f"Occupation: {self.occupation}")

      def speak(self):
        print("Father speaks carefully.")

father_obj = Father('John', 50, 'Engineer')
print(father_obj.show_details())  # uses parents method
print(father_obj.showOccupation()) # uses own child method
print(father_obj.speak())          # uses own child method

#Hierarchichal Inheritence Example
class Grandfather:
      def __init__(self,name,age):
          self.name=name
          self.age = age

      def show_details(self):
          return f'Name: {self.name}, Age: {self.age}'

      def speak(self):
           return 'Grandfather speaks wisely'

class Child1(Grandfather):
      def __init__(self,name,age,hobby):
          super().__init__(name,age)
          self.hobby = hobby

      def show_hobby(self):
          return f'Hobby: {self.hobby}'

      def speak(self):
          return 'Child1 speaks enthusiastically'

class Child2(Grandfather):
     def __init__(self,name,age,favorite_subject):
         super().__init__(name,age)
         self.favorite_subject=favorite_subject

     def show_favorite_subject(self):
         return f'Favorite SUbject: {self.favorite_subject}'

     def speak(self):
         return 'Child 2 speaks thoughtfully'

child1_obj = Child1('Alice',20,'Painting')
child2_obj = Child2('Bob',22,'Mathematics')
print(child1_obj.show_details())
print(child1_obj.show_hobby())
print(child1_obj.speak())


print(child1_obj.show_details())
print(child1_obj.show_favorite_subject())
print(child1_obj.speak())
