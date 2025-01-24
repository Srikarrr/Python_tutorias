#Input : test_list = [(6, 7), (2, 3), (7, 6)] 
#Output : {(6, 7)} 


#Input : test_list = [(6, 7), (2, 3)] 
#Output : {}

# Method #1: Using dictionary comprehension + set()

test_list = [(6,7), (2,3), (7,6), (9,8), (10,2), (8,9)]
temp=set(test_list) & {(b,a) for a,b in test_list}
res ={(a,b) for a,b in temp if a<b}

print("The Symmetric tuples : " + str(res))

temp_set = set()
res = []
for tpl in test_list:
    if tpl in temp_set or (tpl[1],tpl[0]) in temp_set:
        res.append(tpl)
    else:
        temp_set.add(tpl)    


#using recursion
 
def orderer_tuples(test_list, result=[]):
    if len(test_list) == 0:
       return result
    else:
        first, *rest=test_list
        if tuple(sorted(first)) == first:
            result.append(first)
        return orderer_tuples(rest, result)

test_list = [(5, 4, 6, 2, 4), (3, 4, 6), (9, 10, 34), (2, 5, 6), (9, 1)]
res=orderer_tuples(test_list)    
print("Ordered tuples : "+ str(res))
