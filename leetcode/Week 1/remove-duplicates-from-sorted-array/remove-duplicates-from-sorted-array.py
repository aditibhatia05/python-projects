# 07012023
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        unique_elements = 0
        while i<len(nums):
            if j == len(nums):
                unique_elements+=1
                break
            else:
                while j<len(nums) and nums[i]==nums[j]:
                    nums.pop(j)
                unique_elements+=1
                i+=1
                j+=1
        return (unique_elements)
