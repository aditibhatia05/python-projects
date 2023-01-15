# 10012023
# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        unique_elements=0
        i = 0
        j=0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                i-=1
            i+=1
        while j < len(nums):
                unique_elements+=1
                j+=1
        return(unique_elements)



