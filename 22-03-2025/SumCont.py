# list 3,4,7,2,-3,1,4,2  0,3,3+4=7,3+4+7=14,3+4+7+2=16,3+4+7+2-3=13,3+4+7+2-3+1=14,3+4+7+2-3+1+4=18,3+4+7+2-3+1+4+2=20
# final list {0,3,7,,14,16,13,14,18,20}
# dict{0:1,3:1,7:3,14:2,16:1,13:1,18:1,20:1}

from typing import List

class SumCont:
      def subarraySum(self,nums:List[int],k:int) -> int:
            sumdict = {0,1}
            n= len(nums)
            count=0
            s=0

            for num in nums:
                  s+=num
                  if s-k in sumdict:
                      count+=sumdict[s-k]
                  if s in sumdict:
                        sumdict[s]+1
                  else:
                        sumdict[s]=1          