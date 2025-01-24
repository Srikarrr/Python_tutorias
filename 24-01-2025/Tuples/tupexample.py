t = (1,2,3,4,5)

#tuples are indexed
print(t[1])
print(t[4])

#tuples contain duplicate elements
t = (1,2,3,4,2,3)
print(t)

#updating an element this will provide an error
t[1]=100
print(t)

t = (10, 5, 20)

print("Value in t[-1] = ", t[-1])
print("Value in t[-2] = ", t[-2])
print("Value in t[-3] = ", t[-3])

t = (10, 5, 20)

print("Value in t[0] = ", t[0])
print("Value in t[1] = ", t[1])
print("Value in t[2] = ", t[2])

#List Traversal

t= (1,2,3,4,5)
for x in t:
    print(x,end=" ")


#Concatenation of Python Tuples

t1=(0,1,2,3)
t2=('python','geek')

print(t1+t2)

#code for creating nested tuples
t1=(0,1,2,3)
t2=('python','geek')
t3=(t1,t2)
print(t3)

#code for creating tuple with repetition
t=('python',)*3
print(t)

#slicing tuples in Python divided the tuple into small tuples using the index method

t = (0,1,2,3)

print(t[1:])
print(t[::-1])
print(t[2:4])

#outout

#(1, 2, 3)
#(3, 2, 1, 0)
#(2, 3)

# Code for deleting a tuple
t = ( 0, 1)

del t
print(t) # error will come

# Code for printing the length of a tuple
t = ('python', 'geek')
print(len(t))

# tuple with different datatypes
t = ("immutable", True, 23)
print(t)

#('immutable', True, 23)

a = [0,1,2]
t=tuple(a)
print(t)

#output (0, 1, 2)

#Tuples in a loop

t=('gfg',)

#Number of time loop runs

n=5
for i in range(int(n)):
    t =(t,)
    print(t)

#output
# 
#(('gfg',),)
#((('gfg',),),)
#(((('gfg',),),),)
#((((('gfg',),),),),)
#(((((('gfg',),),),),),)
#     

#Using round brackets

t = ("gfg", "Python") 
print(t)

#Using comman separated

# Creating a tuple without brackets
t = 4, 5, 6
print(t)  # Output: (4, 5, 6)

#using tuple constructor

# Creating a tuple using the tuple() constructor
t = tuple([7, 8, 9])
print(t)  # Output: (7, 8, 9)

#Empty Tuple
# Creating an empty tuple
t = ()
print(t)  # Output: ()

#Single Element Tuple

# Creating a single-element tuple
t = (10, ) # Comma is important here
print(t)  # Output: (10,)
print(type(t))

# What if we do not use comma
t = (10) # This an integer (not a tuple)
print(t)  
print(type(t))

#Tuple Packing

# Tuple packing
a, b, c = 11, 12, 13
t = (a, b, c)
print(t)  # Output: (11, 12, 13)