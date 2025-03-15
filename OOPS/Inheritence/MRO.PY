class A:
     def __init__(self):
         self.value='A'

class B(A):
     def __init__(self):
         super().__init__()
         self.value='C'

class C(A):
     def __init__(self):
        super().__init__()
        self.value='C'

class D(B,C):
      def __init__(self):
           super().__init__()

obj = D()
print(obj.value) # goes to D -> then goes to B -> then goes to C -> then goes to A -> the goes to object
