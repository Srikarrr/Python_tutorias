#[-2,1,-3,4,-1,2,1,-5,4]
#take maximum value index of max(max_sum till previuos + index,index)
# at index 0 = -2
# at index 1 =  1 -2+1 = -1<1
# at index 2 = -2  1+-3(-2)>-3
# at index 3 =  4  -3+4<4
# at index 4 =  3   4+-1<4
# at index 5 =  5    3<5
# at index 6 =  6    5<6
# at index 7 =  1    -5<1
# at index 8 =  5    1<5 
from typing import List


class MaxSubArr:
        def maxsunarray(self,nums:List[int])->int:
                total_sum = max_sum = nums[0]
                for i in nums[1:]:
                        total_sum = max(i,total_sum+i)
                        max_sum=max(max_sum,total_sum)

                return max_sum        
