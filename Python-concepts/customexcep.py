class MyCustomError(Exception):
      pass

def somefunction():
      raise MyCustomError('Something went wrong')

try:
    somefunction()
except MyCustomError as e:
      print(f"Caught an exception")      

#adding logic
class InvalidAgeError(Exception):
      def __init__(self,age,message="Age is Invalid"):
            self.age = age
            self.message = message
            super().__init__(self.message)

#Function that raises custom exception

def checkage(age):
      if age < 0 or age > 150:
            raise InvalidAgeError(age,"Age must be between o and 150.")
      else:
         print("Age is Valid")               

# Handling the custom exception
try:
    checkage(200)
except InvalidAgeError as e:
    print(f"Error: {e} (Age: {e.age})")         