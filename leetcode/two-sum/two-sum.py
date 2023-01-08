class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in output: 
                return [output[r], i]
            output[j] = i
