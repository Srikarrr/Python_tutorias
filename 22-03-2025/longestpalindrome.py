# Python

class solution:
    def longestpalindrome(self,s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd lenght
            l,r= i, i
            while l>=0 and r< len(s) and s[l] == s[r]:
                  if( r- l +1)> resLen:
                       res = s[l:r+1]
                       resLen = r-l+1
                  l-=1
                  r+=1

           #even lenght
            l,r = i, i+1
            while l>=0 and r < len(s) and s[1] == s[r]:
                 if(r-l+1) >resLen:
                      res = s[l:r+1]
                      resLen = r-l+1
                 l -=1
                 r +=1

            return res                      
        
        
# Java
Class Solution{
     public String longestPalindrome(String s){
          
     }
}        