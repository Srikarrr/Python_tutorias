class User:
      def __init__(self,name,id,age,passCode):
      self.name=name
      self.id=id
      self.age=age
      self.passCode=passCode

      def login(self):
          print("logged in")

      def logout(self):
          print("logged out")


class Student(User):
      def __init__(self,marks,rollNumber,name,id,age,passCode):
          super().__init__(name,id,age,passCode)
          self.marks = marks
          self.rollNumber = rollNumber

          self.name = name
          self.id   = id
          self.age  = age
          self.passCode = passCode

      def login(self):
          print("OTP SENT")
          print("Student Looping In")
          super.login()


s1= Student(90,123,"Mayank",1,25,"0000")
s1.name

s1.login()
s1.logout()
#s1.play()

u1 = user()
u1.login()

#u1.play()