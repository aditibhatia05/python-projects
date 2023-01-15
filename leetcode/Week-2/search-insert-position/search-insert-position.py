# 11012023
# https://leetcode.com/problems/search-insert-position/submissions/876458381/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_index = 0
        last_index=len(nums)-1
        if start_index == last_index:
            if target<=nums[start_index]:
                return(0)
            else:
                return(1)
            
        while last_index!=start_index:
            mid = (last_index+start_index)//2
            if target == nums[mid]:
                return(mid)
                break
            elif nums[0]>target:
                return(0)
                break
            elif nums[-1]<target:
                return(len(nums))
                break
            elif nums[mid] < target and nums[mid+1] > target:
                return(mid+1)
                break
            elif target < nums[mid]:
                last_index=mid
                continue
            elif target > nums[mid]:
                start_index = mid+1
                last_index=len(nums)-1
                if last_index==start_index and nums[last_index]==target:
                    return(last_index)

            



# with O(n)complexity
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         i=0
#         while i<=len(nums)-1:
#             if nums[i] == target:
#                 return(i)
#                 break
#             elif nums[-1]<target:
#                 return(len(nums))
#                 break
#             elif nums[i] < target and nums[i+1] > target:
#                 return(i+1)
#                 break
#             elif nums[0]>target:
#                 return(0)
#                 break
#             i+=1