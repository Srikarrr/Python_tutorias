#Input : test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )], K = 2 
#Output : [(34, 55), (12, 45), (78,)] 
#Explanation : All tuples have numbers with 2 digits.
#Input : test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (782, )], K = 3 
#Output : [(782,)] 
#Explanation : All tuples have numbers with 3 digits. 

#Method-1

test_list = [ (54,2) , (34,55), (222,23), (12,45), (78, )]

#printing original list
print("The Original list is" + str(test_list))

#Initializing K
k=2

#using len() and str() to check length and perform string conversion
res = [sub for sub in test_list if all(len(str(ele)) == k for ele in sub)]

#printing result
print("The Extracted Tuples : " +str(res))

#Time Complexity: O(n) where n is the number of elements in the list “test_list”.  list comprehension + all() performs n number of operations.
#Auxiliary Space: O(n), extra space of size n is required

#Method #2 : Using all() + filter() + lambda

res = list(filter(lambda sub: all(len(str(ele))== k for ele in sub), test_list))

#Method 3 using list(),map(),str() amd len() 

test_list = [(54,2), (34,55), (222,23), (12,45), (78, )]
print("The Original list is : " +str(test_list))

K=2
res=[]
for i in test_list:
    x=list(map(str,i))
    p=[]
    for j in x:
        p.append(len(j))
    if(p==[K,K] or p==[K]):
        res.append(i)

    print("The Extracted tuples : " + str(res))


# Method#4:Using a for loop and string slicing

#Initialize the list of tuples
#Initialize the value to K=2
#Initialize an empty list called res to store the extracted tuples
#for each tuple in the list setthe flag to true
#for each element in the tuple check if the lenght of the string rep of the element equal to k if its not set the flag to false
# and break out of the loop
# if the flag is still true after checking all the elements of the tuple, append the tuples to the res list
# print the extracted tuples

test_list= [(54,2) , [34,55] , (222,33), (12,45) , (78, )]
print("The Original list is : "+str(test_list))
K=2
res = []
for tup in test_list:
    flag = True
    for ele in tup:
        if(len(str(ele))!=K):
            flag = False
            break

        if flag:
            res.append(tup)


    print("The Extracted Tuples : "+str(res))         
  
