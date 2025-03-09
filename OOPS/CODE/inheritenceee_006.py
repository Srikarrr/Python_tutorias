class complexnum:
      def __init__(self,real,imag):
          self.imag = imag 
          self.real = real

      def __str__(self):  # it will called when print function is called magic method
          if(self.real==0):
              return f"(self.imag)i"
          elif(self.imag<0):
           s = f"(self.real) - (self.imag)i"
          else:
           s = f"(self.real) + (self.imag)i"
          return s
      

      
      def conjugate(self):
          return complexnum(self.real,-1*self.imag) 

      def __add__(arg1,arg2):
          resultReal = 0
          resultImag = 0
          resultReal  =arg1.real+arg2.real
          resultImage =arg1.imag+arg2.imag
          ans = complexnum(resultReal,resultImag)
          return ans
      
      def __sub__(arg1,arg2):
          resultReal = 0
          resultImag = 0
          resultReal  =arg1.real-arg2.real
          resultImage =arg1.imag-arg2.imag
          ans = complexnum(resultReal,resultImag)
          return ans
                 
      def __mul__(self,other):
          resultReal=0;
          resultImag=0;

          resultReal = self.real * other.real  - self.imag*other.imag
          resultImag = self.real * other.image + other.real*self.imag
          ans=complexnum(resultReal,resultImag)
          return ans

      def __truediv__(self,other):
          resultReal=0;
          resultImage=0;
          den = other.real**2+other.imag**2
          ans = self * complexnum(other.real/den,(-1*other.imag)/den)   

      def __eq__(self,other):
          return (self.real == other.real) and (self.imag == other.imag)

      def __neq__(self,other):
          pass         
                 
c=complexnum(3,4)
cn2 =  complexnum(4,5)
print(c+cn2)
c.real,c.imag
print(c)
c.conjugate()

# 1+1 o/p = 2
# "1" + "1" = 11

