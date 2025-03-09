class User:
      def __init__(self):
          print("User Constructor")
          self.website  = "www.flipkart.com"
          self._field    = "ecommerce" #protected member
          self.__duration = "12 months" #private

      def login(self):
          print("logged in")

      def logout(self):
          print("logged out")

class Buyer(User):
      def __init__(self):
          print("Buyer Constructor")
          super().__init__
          self.website="www.amazon.in"
          self.__name="Buyer"

      def login(self):
          super().logout()

      print(self._field) # accessible
      print(self.__name) # not accessible as it is private
