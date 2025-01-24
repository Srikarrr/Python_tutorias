#to extract only extreme K elements, i.e maximum and minimum K elements in Tuple.
#Input : test_tup = (3, 7, 1, 18, 9), k = 2 
#Output : (3, 1, 9, 18)

#Input : test_tup = (3, 7, 1), k=1 
#Output : (1, 7) 

#Method #1 : Using sorted() + loop 

#initializing tuples
test_tup=(5,20,3,7,6,8)
print("The Original tuple is: "+ str(test_tup))

#Initializing K
k=2

#Maximum and Minimum K elements in Tuple
res=[]
test_tup = list(sorted(test_tup))

#after sorting test_tup=(3,5,6,7,8,20)

for idx, val in enumerate(test_tup):
    if idx < K or idx>=len(test_tup) - K:
       res.append(val)
    res=tuple(res) 

    # Printing results
    print("The Extrated Values are : "+str(res))   

#Time complexity: O(n log n) where n is the length of the input tuple. 
#Auxiliary space: O(n) where n is the length of the input tuple

# Method #2 : Using list slicing + sorted() 

#we perform the task of max, min extraction using slicing rather than brute force loop logic.

#initializing Tuple
test_tup = (5,20,3,7,6,8)
print("The Original tuple is : "+str(test_tup))
K=2

test_tup = list(test_tup)
temp=sorted(test_tup)
res= tuple(temp[:K]+temp[-K:])

# printing result 
print("The extracted values : " + str(res))

#Time complexity: O(n log n), where n is the length of the tuple. 
#Auxiliary space: O(n), where n is the length of the tuple. 

