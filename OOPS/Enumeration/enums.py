from enum import Enum

class Days(Enum):
      MONDAY    =1
      TUESDAY   =2
      WEDNESDAY =3
      THURSDAY  =4
      FRIDAY    =5
      SATURDAY  =6
      SUNDAY    =7

print(Days.MONDAY)       # Output: Days.MONDAY
print(Days.MONDAY.name)  # Output: MONDAY
print(Days.MONDAY.value) # Output: 1     


#Enumerations can be compared based on their values or their identities.

if Days.MONDAY is Days.TUESDAY:
    print("Same day!")
else:
    print("Different days!")


if Days.MONDAY == Days(1):
     print("Same day!")

#Auto Value generation

from enum import Enum, auto
class AutoDays(Enum):
     MONDAY    = auto()
     TUESDAY   = auto()
     WEDNESDAY = auto()

print(AutoDays.MONDAY.value)
print(AutoDays.TUESDAY.value)

#Enum.__members__
print(Days.__members__)
 # Output: {'MONDAY': <Days.MONDAY: 1>, 'TUESDAY': <Days.TUESDAY: 2>, ...}

 #example in Computer vision

#1. Classifying Object Categories:

from enum import Enum

class ObjectClass(Enum):
    CAR = 1
    PERSON = 2
    DOG = 3
    CAT = 4

#2 State Representation in Vision Systems:

class RobotState(Enum):
    IDLE = 0
    MOVING = 1
    OBSTACLE_DETECTED = 2
    STOPPED = 3



# Different Types of Image Processing Techniques:

class ImageOperation(Enum):
    GAUSSIAN_BLUR = 1
    EDGE_DETECTION = 2
    THRESHOLDING = 3

# Feature Labeling or Grouping:

class FacialFeatures(Enum):
    LEFT_EYE = 1
    RIGHT_EYE = 2
    NOSE = 3
    MOUTH = 4   

# In complex systems, error handling or status codes can be used in conjunction with enums to clearly identify 
# different states or errors encountered during computer vision tasks

class DetectionStatus(Enum):
    SUCCESS = 1
    NO_FACE_DETECTED = 2
    LOW_CONFIDENCE = 3
    PROCESSING_ERROR = 4

# Setting Parameters in Vision Models:
 
class ModelArchitecture(Enum):
    RESNET = 1
    VGG = 2
    EFFICIENTNET = 3
    
#Defining Regions of Interest (ROIs):

class ROIType(Enum):
    FACE = 1
    LICENSE_PLATE = 2
    BARCODE = 3


 #Enum with Methods

from enum import Enum

class Color(Enum):
      RED   =1
      GREEN =2
      BLUE  =3 
 
      def describe(self): 
         return f"The color is {self.name}"   
      
      def is_primary(self):
          return self in {Color.RED, Color.GREEN, Color.BLUE}
      
color = Color.RED
print(color.describe()) # Output: The color is RED.
print(color.is_primary())  # Output: True    

#Enum with Custom Values hold tuples, strings

from enum import Enum

class Currency(Enum):
      USD=('United States Dollar','USD',1)
      EUR=('Euro','EUR',0.85)
      JPY=('Japanese Yen','JPY',110)

      def __init__(self,name,symbol,conversion_rate):
          self.name_full = name
          self.symbol    = symbol
          self.conversion_rate = conversion_rate

      def describe(self):
          return f"{self.name_full} ({self.symbol}) - Conversion rate: {self.conversion_rate}"

currency = Currency.USD
print(currency.describe())          

# Enum with Automatic Values By default auto generates increasing integers

from enum import Enum, auto

class Fruit(Enum):
      APPLE  = auto()
      BANANA = auto()
      CHERRY = auto()

      @classmethod
      def _generate_next_value(cls,start,count,last_values):
          return f"Fruit_{count+1}"
      
print(Fruit.APPLE.value)  #Output: Fruit_1
print(Fruit.BANANA.value) #Output: Fruit_2

#Enum with Unique Values (@unique)

#If you want to ensure that all values in an enum are unique 
# (i.e., no two members have the same value), you can use the @unique decorator 
# from the enum module. This is helpful for detecting and preventing unintended value 
# duplication.

from enum import Enum, unique

@unique
class Status(Enum):
      PENDING     = 1
      IN_PROGRESS = 2
      COMPLETED   = 3
      CANCELED    = 4

# This would raise a ValueError because two members cannot have the same value
@unique
class InvalidStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    DUPLICATE = 3



#Enum with Custom Comparison Logic You can also customize how enum members are compared by overriding the comparison methods (__eq__, __lt__, etc.). This can be useful for more complex use cases
#where you need custom comparison behavior.
from enum import Enum

class Priority(Enum):
     LOW    = 1
     MEDIUM = 2
     HIGH   = 3

     def __lt__(self,other):
          if not isinstance(other,Priority):
               return NotImplemented
          return self.value<other.value
     
# Usage
print(Priority.LOW < Priority.MEDIUM)  # Output: True
print(Priority.HIGH < Priority.MEDIUM)  # Output: False
