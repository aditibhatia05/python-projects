class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        j = len(x1)
        for i in range(0, j):

            if x1[i] != x1[j-1]:
                return False
            else:
                j = j-1
        return True
