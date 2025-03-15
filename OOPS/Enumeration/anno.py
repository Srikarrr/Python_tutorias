#In Python, annotations are a way to attach metadata to function arguments and return types.
#These are often used for type hinting, but you can also create custom annotations 
#for purposes beyond typing, such as validation, logging, or documentation.

#Simple Custom Annotations

class MinValue:
      def __init__(self,value):
            self.value=value

      def __repr__(self):
            return f"MinValue({self.value})"

class MaxValue:
      def __init__(self,value):
            self.value=value

      def __repr__(self):
            return f"MaxValue({self.value})" 

# Function with custom annoatations

def process_data(data: int, threshold: MinValue(10), limit: MaxValue(100)) -> bool:
    print(f"Processing {data} with min value {threshold} and max value {limit}")
    return threshold.value <= data <= limit.value

# Accessing custom annotations
print(process_data.__annotations__)                      

#Using Custom annotations for validation

class Positive:
      def __init__(self):
            pass
      
      def __repr__(self):
            return "Positive()"
      
      def validate_annotations(func):
           def wrapper(*args, **kwargs):
               annotations = func.__annotations__
               for arg_name,arg_value in zip(func.__code__.co_varnames,args):
                   annotation = annotations.get(arg_name)
                   if isinstance(annotation,Positive) and arg_value <= 0:
                        raise ValueError(f"{arg_name} should be positive, but got {arg_value}")
               return func(*args, **kwargs)
           return wrapper           
      

# Function with custom annotation
@validate_annotations
def deposit(amount: int) -> None:
    print(f"Depositing {amount} units.")

# Test the function
deposit(100)  # Works fine
deposit(-10)  # Raises ValueError: amount should be positive, but got -10