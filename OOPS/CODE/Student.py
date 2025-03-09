class Student:
       numberOfStudents = 0 # at the class level to use this we need to access with student class
       schoolName = "MAPS"

       def __init__(self,name,rollNumber,marks):
             #print(id(self))
             #numberOfStudents = 0 # at the constructor level
             self.name = name 
             self.rollNumber = rollNumber
             self.__marks = marks
             self.numberOfStudents         = Student.numberOfStudents  + 1
             Student.numberOfStudents      = Student.numberOfStudents  + 1

       def study(self):
           print("I am  "+self.name +" and I am Studying") 

       def play(self):
           print(f"self.name  is Playing")               

       def getMarks(self):
            return self.__marks
                  
       def setMarks(self,newmarks,passcode):
           if(passcode == self.__auth):
              self.__marks=newmarks  
           else:
              print("unable to submit")     
           self.__marks= newmarks      

       def __auth(self):
            return "0000"         

s1=Student("Mayank",1,90)    
s2=Student("Goku",2,50)

s1.marks
s2.marks
s1.marks=45

#Student.schoolName
#print(s1.getMarks())
#s1.marks = 45
#print(s1.getMarks())
#s1.setMarks(95,"0001")
#s1.getMarks()
# lets say you have bank account application now you need to safeguard those variable now you need to safeguard
# the marks variable 


