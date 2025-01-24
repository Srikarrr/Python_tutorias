# Python program to reverse a linked list 
# Time Complexity : O(n) 
# Space Complexity : O(n) as 'next'  
#variable is getting created in each loop. 
  
# Node class 

class Node:

      def __init__(self,data):
          self.data=data
          self.next=None


class LinkedList:
     
      def __init__(self):
          self.head=None

      def reverse(self):
          prev=None
          current=self.head
          while(current is not None):
                next= current.next
                current.next=prev
                #swap the data
                prev=current
                current=next
                #make head is previous
                self.head=prev     

      # Function to insert a new Node at the beginning

      def push(self,data):
          new_node=Node(data)
          new_node.next=self.head
          self.head=new_node

     # Utility function to print the Linked List
      def printList(self):
           temp = self.head
           while(temp):
                print (temp.data,end=" ")
                temp= temp.next

     # Driver program to test above functions

      llist = LinkedList()
      llist.push(20)
      llist.push(4)
      llist.push(15)
      llist.push(85)

      print("Given Linked List")
      llist.printList()
      llist.reverse()
      print("\nReversed Linked List")
      llist.printList()             
           
                          