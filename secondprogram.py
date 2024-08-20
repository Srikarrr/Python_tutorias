str1="this is a string.\n we are creating it in python"
str2='apna college'
str3="""this is a string"""
str4='this is apnacollege"s tutorial'
str5="this is a string.\t we are creating it in python"
#this will throw an error because of apostrope
#str5="this is apnacollege"s tutorial"

print(str1)
print(str5)

# concatenation

str1="apna"
len1= len(str1)
print(len1)

str2="college"
len2= len(str2)
print(len2)

final_str=str1+str2
print(final_str)

final_str=str1+ " "+ str2
print(len(final_str))


#char index
str8="apna college"
ch1=str8[1]
ch2=str8[4]
ch3=str8[5]
print(ch1)
print(ch2)
print(ch3)

# error as we cannot manipulate characters TypeError: 'str' object does not support item assignment
# str8[5]="@"

str="apna college"
print(str[1:4])
# 
print(str[5:12])
print(str[5:len(str)]) 
print(str[5:]) # by default space at end will take len(str)
print(str[:4]) # by default space at beg will take 0

print(str[-5:-2])

str="i am studying python with Apna College"
print(str.endswith("app"))
print(str.capitalize())
print(str)
str=str.capitalize()
print(str)

print(str.replace("python","javascript"))

light = "pink"
if(light == "red"):
  print("stop")
elif(light == "green"):
  print("go")
elif(light == "yellow"):
  print("look")
else:
  print("light is broken")  


age = 14
if(age>=18):
  print("can vote")
else:
  print("cannot vote")  

marks = input("enter student marks: ")
if(marks >= 90):
  grade = "A"
elif(marks>=80 and marks<90):
  grade = "B"
elif(marks>=70 and marks <80):
  grade = "C"
else:
  grade = "D"
print("grade of the student ->",grade)

#nesting if under if
if(age >= 18):
   if(age>=80):
      print("cannot drive")
   else:
      print("can drive")
else:
   print("cannot drive")           



num=int(input("Enter Number"))
rem = num % 2
if(rem == 0):
  print("EVEN")
else:
  print("ODD")  

#print biggest of 3 numbers
  
a = int(input("enter first number  : "))
b = int(input("enter second number : "))
c = int(input("enter third number :  "))

if(a>=b and a>=c):
  print("first number is bigger",a)
elif(b>=c):
  print("second number is largest",b)
else:
  print("third is largest",c)

x=int(input("Enter Number"))
  
if(x % 7 == 0):
  print("multiple of 7")
else:
  print("not a multiple") 