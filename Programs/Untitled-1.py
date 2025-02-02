class Node:
      def __init__(self,next=None,prev=None,data=None):
                   self.data=data
                   self.next=None
                   self.prev=None


      def traverse(head):
        current=head      
        while current:
               print(current.data,end="< - >")
               current=current.next
               print("None")


      def insert_at_beginning(head,data):
          new_node=Node(data)
          new_node.next = head
          if head:
                head.prev = new_node
          return new_node                           
      

      # Driver Code
      head = None
      head = insert_at_beginning(head,4)
      head = insert_at_beginning(head,3)
      head = insert_at_beginning(head,2)
      head = insert_at_beginning(head,1)

      traverse(head)

  #Python Program for a doubly linked list
   
class Node:
      
      def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None


      def insert_at_beginning(head,data):
           new_node = Node(data)
           new_node.next=head
           if head:
                 head.prev=new_node
           return new_node        
       
      def display(head):
           current= head
           while current:
                 print(current.data, end=" <->")
                 current=current.next
           print("None")


      #Driver Code

           head=None
           head= insert_at_beginning(head,3) # type: ignore
           head= insert_at_beginning(head,2) # type: ignore
           head= insert_at_beginning(head,1) # type: ignore

           print("Double Linked List after insertion at the beginning:")
           display(head) # type: ignore
                        