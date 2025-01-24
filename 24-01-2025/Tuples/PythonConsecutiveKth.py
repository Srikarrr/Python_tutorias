#Input : test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)], K = 0 
#Output : [4, 4, 2] 
#Explanation : 5 – 1 = 4, hence 4. 


#Input : test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)], K = 2 
#Output : [2, 4, 5] 
#Explanation : 8 – 3 = 5, hence 5. 

#Method-1 Using Loop

#StepByStep approach

#Initializes a variable to K+1 which represents the index of the column we want to compare
#Creates an empty list res to store the absolute differences
#Loops through the range of indices from 0 to the second-to-last of index of the list using a loop and the range() function.
#Inside the loop, the program calculates the absolute difference between the Kth column of the current tuple and the Kth column of the next 
#tuple using the abs() funtion and appends the result to the res list
#After the Loop Finishes, The Program prints the resultant tuple list using the print() function and str() function to convert the list to a string

import numpy as np

test_list = [ (5,4,2), (1,3,4), (5,7,8), (7,4,3)]
res=[]
K=1
for idx in range(0,len(test_list)-1):
    res.append(abs(test_list[idx][k]-test_list[idx + 1][K]))


res = [abs(x[K]-y[K]) for x,y in zip(test_list,test_list[1:])]

arr= np.array(test_list)
res= np.abs(np.diff(arr[:,K]))

#Using List Slicing
#Initialize an empty list "res" to store the result
#Initialize "K" to the required value
#Iterate over the range from 0 to the lenght of the "test_list" minus K
#within the loop, use list slicing to get the Kth column from the current Tuple and the next tuple, then calculate the abs difference b/w using abs() fucntion
#append the difference to the res list
#return the res list as the result

test_list=[(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]
K=1
res= [abs(test_list[i][K] - test_list[i+1][K]) for i in range(len(test_list)-K)]
print("Resultant tuple list : " + str(res))