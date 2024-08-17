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