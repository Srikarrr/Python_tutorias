#sort the array []
#take 2 pointers start from left and right
#left = i+1, right=last element
#sumtotal = i+i+1+r
#sumtotal = 0(target) L=L+1,R=R-1
#sumtotal<0 L=L+1
#sumtotal>0 R=R-1
#sumtotal ==0 result.append(nums[i]nums[l][nums[r])

from typing import List


class sumsolution:
      def threesum(self,nums:List[int]) -> List[List[int]]:
            res=[]
            nums.sort()
            lenght = len(nums)

            for i in range(lenght-2): # make two pointers left anf right which should be ahead of i
                  #edge cases
                  if i>0 and nums[i]==nums[i-1]:
                      continue
                  i=i+1
                  l=i+1
                  r=lenght-1

                  while l<r:
                        total = nums[i]+nums[l]+nums[r] 
                        if total<0:
                            #-2,-1,0,1
                            l=l+1
                        elif total>0:
                            r=r-1
                        else:
                             res.append([nums[i],nums[l],nums[r]])
                             while l<r and nums[l]==nums[l+1]:
                                  l=l+1
                             while l<r and nums[r]==nums[r-1]:
                                  r=r-1;

                             l = l+1
                             r = r-1    
                    
                  return res                   

                  