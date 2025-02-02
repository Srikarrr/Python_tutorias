marks = [94.4,87.5,95.2,66.4,45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

#in C++/JAVA arrays should be of same type but in 
#python we can store different types of items in a string

student = ["karan",95.4,17,"Delhi"]
print(student[0])
student[0]="arjun"
print(student)

str="hello"
print(str[0])
#str[0]="y" this wont happen as string is immutable

list = [2,1,3]
list.insert(1,5)
print(list)

#expected output 2,5,1,3
list = [2,1,3,1]
list.remove(1) #removes first occurance of element [2,3,1]
list.pop(idx) #removes element at idx
#example 
list.pop(2) # output 2,1,1 

#tuples

tup = (2,1,3,1)
print(tup[0])
print(tup[1])
tup[0] = 5 #not possible gets error tuple object does not support item assignments

tup(1)
print(tup)
print(type(tup))

#o/p class 'int'

tup(1)
print(tup)
print(type(tup))

#o/p class 'int'

tup(1,)
print(tup)
print(type(tup))

#o/p class 'tuple'

tup(1.0)
print(tup)
print(type(tup))

#o/p class 'float'

tup("hello")
print(tup)
print(type(tup))

#o/p class 'string'

tup(1,2,3,4)
print(tup[1:3])

#Methods

tup = (2,1,3,1)

tup.index(1) #returns index of first occurence tup.index(1) is 1
tup.count(1) #count total ouucerances

#example-1

movies = []
mov1=input("enter 1st movie")
mov2=input("enter 2nd movie")
mov3=input("enter 3rd movie")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#palindrome

list1 = ["m","a","a","m"]
copy_list=list1.copy()
copy_list.reverse()
if(copy_list == list1):
  print("palindrome")
else:
  print("not palindrome")      

grade = ["C","D","A","A","B","B","A"] 
print(grade.count("A"))
grade.sort();
