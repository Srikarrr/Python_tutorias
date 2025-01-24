coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')

# this is about slicing

#blue coral-0,staghorn coral-1,pillar coral-2,elkhorn coral-3
#Negative Indexing #blue coral -4,staghorn coral -3 ,pillar coral -2 ,elkhorn coral -1

print(coral[1:3])
#Output ('staghorn coral', 'pillar coral')

# [1:3]  1 represents starting index and 3 represents ending index

print(coral[:3])
#('blue coral', 'staghorn coral', 'pillar coral')
#This printed the beginning of the tuple, stopping right before index 3.

print(coral[1:])

#('staghorn coral', 'pillar coral', 'elkhorn coral')

print(coral[-3:-1])
#('staghorn coral', 'pillar coral')
print(coral[-2:])
#('pillar coral', 'elkhorn coral')


# This is about Stride

#One last parameter that we can use with slicing is called stride,
# which refers to how many items to move forward after the first item is retrieved from the tuple.

#numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
#print(numbers[1:11:2])
#Output (1, 3, 5, 7, 9)

#from where to start - 1 says
#how many items to move forward # 2 represent which is stride
#till where it should move and stop

print(numbers[::3])
#Output (0, 3, 6, 9, 12)

#This is about concatenation

coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
kelp = ('wakame', 'alaria', 'deep-sea tangle', 'macrocystis')
coral_kelp = (coral + kelp)
print(coral_kelp)

#Output ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral', 'wakame', 'alaria', 'deep-sea tangle', 'macrocystis')

#This is about mutliplications as We can mutliply the collections

multiplied_coral = coral * 2
multiplied_kelp = kelp * 3

print(multiplied_coral)
print(multiplied_kelp)

#Output
#('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral', 'blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
#('wakame', 'alaria', 'deep-sea tangle', 'macrocystis', 'wakame', 'alaria', 'deep-sea tangle', 'macrocystis', 'wakame', 'alaria','deep-sea tangle', 'macrocystis')

kelp = ('wakame', 'alaria', 'deep-sea tangle', 'macrocystis')
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print(len(kelp))
print(len(numbers))

more_numbers = (11.13, 34.87, 95.59, 82.49, 42.73, 11.12, 95.57)

print(max(more_numbers)) #95.59
print(min(more_numbers)) #11.12

coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral') #tuple
coral[0] = 'black coral'

coral = ['blue coral', 'staghorn coral', 'pillar coral'] # tuple converted to List

#Output TypeError: 'tuple' object does not support item assignment because Tuples cannot be modified