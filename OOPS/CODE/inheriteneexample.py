class user:
      def __init__(self,name,id,age,passcode):
          self.name = name
          self.id   = id
          self.age=age
          self.passcode=passcode

      def login(self):
           print("P logged in")
           
      def logout():
           print("P logged out")

      def __age(self):
           print("Age")    
      def _property(self):
           print("Property")        

class Student(user):
      def __init__(self,marks,rollnumber,name,id,age,passcode):
          super().__init__(name,id,age,passcode)
          print(super().login())
          self.marks=marks
          self.rollnumber=rollnumber
      
      def play(self):
           print("Playing") 
           self._property()
      
      def login(self):
           print("Student Logging in")    
           super().login() 

s1 = Student(90,123,"Mayank",1,25,"0000")

s1.login()
s1.play()

s1.logout()
s1.__age() # here error will come as it is private

u1 = user();
u1.login()
# this wont happens ul.play()