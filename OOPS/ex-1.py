
from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def login(self):
        pass

    def logout(self):
        print("logout")
    
    @abstractmethod     
    def auth(self):
        pass

class Buyer(User):
     

     def login(self):
          if(self.auth):
            print("Logging in User")

     def check_Object(self,link):
         print(link)

     def auth(self):
          return True  

class Seller(User):
     def login(self):
         if(self.auth):
             print("Logging in Seller") 

     def checkObject(self,link):
         print(link)

     def auth(self):
         print("OTP")
         return True                    
     
b1= Buyer(); # error will come Can't instantiate abstract class Buyer with abstract Methods auth, 
#  login So you need to implement auth 

b1.auth()

#O/P True
    