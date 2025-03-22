def get_squarer_numbers(numbers):
    squared_numbers=[]
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers

numbers=[2,5,8,9]
get_squarer_numbers(numbers)    

#time = a*n+b
#O(N) it takes Order of N iterate all the elements

def find_first_pe(prices,eps,index):
    pe=prices[index]/eps[index]
    return pe

#O(1) since it will find in the first time  
#time = a*n+b  

numbers= [3,6,2,4,3,6,8,9]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]==numbers[j]:
           print(numbers[i]+" is a duplicate")


#time = a*n2+b -> O(n square)            


# 4,9,15,21,34,57,68,91 search for 68

#1st approach iterate all values

for i in range(len(numbers)):
     if numbers[i] == 68:
        print(i)
# O(N)

#THROUGH BINARY SEARCH WHERE WE TAKE THE MID ELEMENT AND THEN compare with search element
#if search  element > MID ELEMENT then MID ELEMENT+1 to len(array)
#else search element < MID ELEMENT then O to MIDELEMENT-1

#4,9,5,(21),34,57,68,91 - Iteration1 = n/2
#34,57,68,91            - Iteration2 = n/2/2 = n/2square
#68,91                  - Iteration3 = n/2/2/2 = ncube 

#so now we will convert this

#Iteration K=n/2k so n=2k
#log2n=log22powerk
#log2n=k*log2power2
#finally O(logn)
#k=O(logn) ->log28->log22powercube(3)->3*log2power2 = 3 iterations

