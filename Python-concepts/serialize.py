import pickle

#serialize
data = {'name': 'Alice', 'age':30}
with open('data.pkl','wb') as f:
     pickle.dump(data,f)


#deserialize
with open('data.pkl','rb') as f:
     loaded_data=pickle.load(f) 
print(loaded_data)     


import json

# Serialize (save) an object
data = {'name': 'Alice', 'age': 30}
with open('data.json', 'w') as f:
    json.dump(data, f)

# Deserialize (load) the object
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
print(loaded_data)