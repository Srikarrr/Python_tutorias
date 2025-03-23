#Given an expected Input array (0,1,2,4,5,6,7) target =3 find =4, find=8 then output below values
# O/P (4,5,6,7,0,1,2) found value 4 at index = 3 , found value 8 at index = -1
# find it in algorithms runtime complexity at Olog(n)


class Solution:
     def search(self,nums: List[int], target:int) -> int:
          l, r = 0, len(nums) - 1

          # [1]    
          while l <= r:
               mid = (l+r)//2
               if target == nums[mid]:
                    return mid
               

               #left sorted position
               if nums[1] <= nums[mid]:
                    if target > nums[mid] or target < nums[l]:
                         left = mid+1
                    else:
                         r = mid - 1  
              #right sorted portion              
               else:          
                    if target < nums[mid] or target> nums[r]:
                          r = mid-1
                    elif target>nums[r]:
                          l = mid+1

               return -1                   