# 12012023
# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return len(s)
        s = s.rstrip()
        j = len(s) - 1
        counter = 0
        # while j > 0:
        #     if s[j] == " ":
        #         j-=1
        #         continue
        #     else:
        #         break
        while j >= 0:
            counter+=1
            if s[j] == " ":
                counter-=1
                break
            j-=1
        return counter