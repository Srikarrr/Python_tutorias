class Item:
     pay_rate=0.8 # The PayRate after 20% Discount
     all=[]
     def __init__(self,name: str,price: float,quantity=0):
          #run validations to the received arguments
          assert price>=0, f"Price {price} is not greater than or equal to Zero!"
          assert quantity>=0, f"Quantity {quantity} is not greater or equal to than Zero!"
          print(f"I AM CREATED: {name}")
          #Assign to self Object
          self.name=name
          self.price=price
          self.quantitiy=quantity

          #Actions to Execute
          Item.all.append(self)# appends the class template

     @property
     #Property Decorator = Read-Only Attribute
     #def name(self): cannot create with the name attribute
     #    return self.name 

     def calculate_total_price(self):
          return self.price*self.quantitiy
          # In Python, self is a parameter that refers to the current instance of a class. 
          # It's used to access a class's methods and variables.
          #The pass statement in Python is a placeholder that indicates a code block is empty or needs to be written in the future
          #__init__ method in Python is used to initialize objects of a class. It is also called a constructo

     def apply_discount(self):
          self.price=self.price * self.pay_rate # Item.pay_rate - this is class object cant change it   

     #To Install CSV use this command pip install csv
     #Inorder to convert this to a class method we need to use a decorator that will be responsible
     
     @staticmethod  # this is a normal method which recieves parameters
     def is_integer(num):
          # We will count out the floats that are point zero
          # For i.e: 5.0, 10.0
          if isinstance(num, float): # check whether number is a float or not
               # Count out the floats that are point zero
               return num.is_integer() 
          elif isinstance(num,int):
               return True
          else:
               return False

     @classmethod #Class Method sending the class reference as a first argument
     def instantiate_from_csv(self): 
          with open('ites.csv','r') as f:
               reader = csv.DictReader(f)
               items  = list(reader)

          for item in items:
              Item(
                   name     =item.get('name'),
                   price    =int(item.get('price')),
                   quantity =int(item.get('quantity')),
              )   

     @property   #These are the read only attribute
     def read_only_name(self):
          return "AAA"   

item1= Item("Phone",100,1) #created instance of class #here it calls Init as it is a constructor
item1.apply_discount();
print(item1.price)
item2=Item("Laptop",1000,3) #created instance of class #here it calls Init as it is a constructor
#item1= Item("Phone",100,-1) # this throws an error
#item2= Item("Phone",100,-3) # this throws an error
item3=Item("Cable",10,5)
item4=Item("Mouse",50,5)
item5=Item("KeyBoard",75,5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

print(Item.all) # gets the instances details

for instance in Item.all:
    print(instance.name)

def __repr__(self): # It will return the no of instances an Item Object has
     return  f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"    

        
#item1.name     = "Phone"
#item1.price    = 100
#item1.quantity = 5
 #created instance of class #here it calls Init as it is a constructor
#item2.name     = "phone"
#item2.price    = 1000
#item2.quantity = 5

random_str     = str("4")
item2.has_numpad=False

print(type(item1)) #item
print(type(item1.name)) #item
print(type(item1.price)) #item
print(type(item1.quantity)) #item

print(item1.name)
print(item2.name)

print(item1.price)
print(item2.price)

print(item1.quantity)
print(item2.quantity)


print(Item.pay_rate)  # FROM Class we can get that variable
print(item1.pay_rate) # FROM Object we can get that variable
print(item2.pay_rate) # FROM Object we can get that variable

print(Item.__dict__)  # All the attributes for class level
print(item1.__dict__) # All the attributes for instance level

random_str = "aaa"
print(random_str.upper())

Item.instantiate_from_csv()
print(Item.all)
print(Item.is_integer(7.0))



#When to use class methods and when to use static methods?
class Item:
      @staticmethod
      def is_integer():
           '''
           This should do something that has a relationship with the class, but not something that must be unique per instance!
           '''

      @classmethod #cls mandatory parameter to receive
      def instantiate_from_something(cls):
           '''
           This should also do something that has a relationship with the class, but usually, those are used to manipulate data structures
           of data to instantiate Objects, like we have done with CSV
           '''     


# HowEver, those could be also called from instances

item1=Item()
item1.is_integer()

#Inheritance
class Phone(Item):
      all = []
      
      #assign to self object
      
      def __init__(self ,name: str, price: float, quantity=0, broken_phones=0):
           super().__init__(
                name,price,quantity
           ) 

      #Run Validations to the received arguments
      assert broken_phones>=0, f"Broken Phones {broken_phones} is not greater than or equal to zero"  # type: ignore
      self.broken_phones = broken_phones     # type: ignore
      Phone.all.append(self) # type: ignore

 
         
phone1=Phone("jscPhonev10",500,5,1)      
print(phone1.calculate_total_price())     

       