class Node:
       def __init__(self,data):
              self.data=data
              self.next=None

class Stack:
       def __init__(self):
           self.head=None 


       def isEmpty(self):
           if self.head == None:
                return True
           else: 
                return False   
           
       def pushData(self,data):
             if self.head== None:
                   self.head=Node(data)
             else:
                   newNode=Node(data)
                   newNode.next=self.head
                   self.head=newNode 

       #Remove element that is the current head (start of the stack)

       def pop(self):
             if self.isEmpty():
                return None    

             else:
                 poppedNode=self.head
                 self.head=self.head.next
                 poppedNode.next=None
                 return poppedNode.data

       #Returns the head node data

       def peek(self):

             if self.isEmpty():
                 return None
             else:
                 return self.head.data

       #prints out the stack data

       def display(self):
            iterNode=self.head
            if self.isEmpty():
                 print("Stack Underflow")
            else:
                 while(iterNode!=None):
                     print(iterNode.data,end="")
                     iterNode=iterNode.next
                     if(iterNode!=None):
                          print(" -> ",end="")
                 return

       #Creating a Stack
       stack = Stack()

       #pushing elements into the stack
       stack.push(10)
       stack.push(20)
       stack.push(30)

       #Displaying the Stack
       stack.display()

       #Peeking at the top element

       print("\nTop Element:",stack.peep())

       #Popping Elements from the Stack

       print("Popped element:"+stack.pop())  
       print("Popped element:"+stack.pop())  

       stack.display()                       


       #Time Complexity: O(1), for all push(), pop(), and peek(), as we are not performing any 
       #kind of traversal over the list. We perform all the operations through the
       #current pointer only.
       #Auxiliary Space: O(N), where N is the size of the stack                        
            