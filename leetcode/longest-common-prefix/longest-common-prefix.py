# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        temp = (min(strs, key=len))
        j = 0
        if len(strs)==1:
            return strs[0]
        for i, j in enumerate(strs):
            if j == "":
                return j
            if j == temp:
                strs.pop(i)
        for i in range(len(temp)):
            for j in range(len(strs)):
                if temp[i] != strs[j][i]:
                    return output  
                elif temp[i] == strs[j][i] and j == len(strs)-1:
                    output = output+strs[j][i]
                else:
                    continue 
        return output   
