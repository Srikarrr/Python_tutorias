#solution
#take 1st character and increase the characters one by one and when we get the 1st character then
# increase it to 2nd character and get the count of previus this technique is called 
# sliding window character technique
#use dictinary to check whether the character is seen or not
#while moving forward we check whether this character is in the dictionary or not
#at the end take out my lenght = i - start +1
class long:
       def lenghtoflongestSubstring(self,s:str)->int:

            if len(s)==0:
                  return 0
            map={}
            max_lenght = start = 0

            for i in range(len(s)):
                  if s[i] in map and start<=map[s[i]]:
                     start = map[s[i]]+1 
                  else:
                      max_lenght = max(max_lenght,i-start+1)
                  map[s[i]]=i
            return (max_lenght)                         
