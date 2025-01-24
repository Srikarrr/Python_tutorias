stock_prices = [] #list
with open ("DataStruct.csv","r") as f:
     for line in f:
          tokens = line.split(',')
          day=tokens[0]
          price=float(tokens[1]);
          stock_prices.append(day,price)

stock_prices

for element in stock_prices:
     if element[0] == 'march 9':
          print(element[1])


#complexity is Order(N)
# Through Dictionary we can use Order(1)          

stock_prices = {} #Dictionary
with open ("DataStruct.csv","r") as f:
     for line in f:
          tokens = line.split(',')
          day=tokens[0]
          price=float(tokens[1]);
          stock_prices[day]=price

stock_prices 

stock_prices['march 9']

#dictionary is more powerful For Dictionary HashTable is implemented how O(1)