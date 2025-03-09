class user:
       def __init__(self):
           print("User Constructor") 
           self.website    = "www.flipkart.com"
           self._field     = "ecommerce"
           self.__duration = "12 Months"
           self.name       = "flipkart User"

       def login(self):
           print("logged in")

       def logout(self):
           print("logged out")

class Buyer:
      def __init__(self):
          print("Buyer Constructor") 
          super().__init__()
          self.website="www.amazon.in"
          self.name="Buyer"

      def login(self):
          super().logout()

          print("mentor logged in")
          print(self._field) #accessible
          print(self.__name) #Not accessible
           

