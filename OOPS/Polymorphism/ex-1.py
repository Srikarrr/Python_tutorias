def sum(a,b):
    print(a+b)

sum(2,3)
def sum(a,b,c): #overrided
    print(a+b+c)

sum(2,3,4)
sum(3,4)          


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
                         
 


                         