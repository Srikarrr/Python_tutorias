class node:
    def __init__(self,data=None):
        self.data=data
        self.none=None  #pointer to the next node

class linkedlist:  #It is a wrapper around Node

    #In the constructor we are always going to have our head node available inside the linked list
    #head node wont be having any data
    #its not going to be indexable

    def __init__(self):
        self.head=node()

    #append function adding a new data point to the end of the data list
    #creates the first element of the list

    def append(self,data):
        new_node=node(data);  #pass the data and it calls the node constructor
        cur=self.head         #stores the left most value in the cur variable
        while cur.next!=None: # iterate each value until last value 
                cur = cur.next
        cur.next = new_node # last element set to new_node

    def length(self):  # length of our linked list
        cur=self.head
        total=0
        while cur.next!=None:
              total+=1
              cur=cur.next

        return total
        
    def display(self):   #helper function to display current context
         elems=[]
         cur_node=self.head
         while cur_node.next!=None:
               cur_node=cur_node.next
               elems.append(cur_node.data)
        
         print (elems)

    def get(self,index):
        if index>=self.length():
            print ("ERROR: 'Get' Index out of range!")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index:
               return cur_node.data
            cur_idx+=1  

    def erase(self,index):
         if index>=self.length():
             print ("ERROR: 'Erase' Index Out of Range!")       
             return    
         
         cur_idx=0
         cur_node=self.head
         while True:
                last_node= cur_node
                cur_node=cur_node.next
                if cur_idx==index:
                   last_node.next=cur_node.next
                   return
                cur_idx+=1     


my_list = linkedlist()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()    

print ("element at 2nd index: %d" % my_list.get(2))

     
        

