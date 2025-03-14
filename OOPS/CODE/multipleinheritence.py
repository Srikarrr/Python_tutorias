class Father:
      def __init__(self,name,age):
          self.name = name
          self.age  = age

      def show_details(self):
           return f'Name {self.name}, Age: {self.age}'

      def speak(self):
           return 'Father speaks carefully'

class Mother:
      def __init__(self,name,favorite_food):
           self.name=name
           self.favorite_food=favorite_food

      def show_favorite_food(self):
           return f'Favorite Food: {self.favorite_food}'

      def speak(self):
           return 'Mother speaks lovingly'

class Child(Father,Mother):
      def __init__(self,name,age,favorite_food,hobby):
           Father.__init__(self,name,age)
           Mother.__init__(self,name,favorite_food)
           self.hobby=hobby

      def show_hubby(self):
           return f'Hobby: {self.hobby}'

      #def speak(self):
      #      return 'Child speaks excitedly'

Child_obj = Child('Daisy',16,'Pizza','Dancing')
print(Child_obj.show_details())
print(Child_obj.show_favorite_food())
print(Child_obj.show_hubby())
print(Child_obj.speak()) # this will go to father class as it is inherited first if its not there then it will go to mother
                                        
