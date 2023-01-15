# 15012023
# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for i in range (1, int(x/2)+2):
            if x > i * i:
                continue
            elif x < i * i:
                break
            elif x == i*i:
                return i
        return i-1