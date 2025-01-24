class stack:
       
      #Method for Pushing data into Stack

      def push(self,st,data):
            st.append(data)

      #Method for pop

      def pop(self,st):
            if len(st)>0:
               ans=st.pop()
               print("Removed element from the st: &quot;", ans)
            else:
               print("The Stack is Empty") 

      
      #Method to get top of stack

      def top(self,st):
           if len(st)>0:
                return st[len(st)-1]
           
      
     #Method to check stack is Empty or not

      def isEmpty(self,st):
         if len(st)==0:
             return 1
         else:
             return 0     

      #Method to get Size of Stack

      def size(self,st):
           return len(st)   
      

 # Creating Object of Stack Class
st= stack()
my_stack=["Lokesh","Diwakar","Aniket","Ritik"]

print(my_stack)
print(st.size(my_stack))
st.pop(my_stack)
print("Top Element in the Stack"+st.top(my_stack))

#check stack is empty or not
print(st.isEmpty(my_stack))

#Push Element into Stack
st.push(my_stack,"Vimal")

#Stack after Push
print(my_stack)

     


                             

        