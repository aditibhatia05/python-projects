# 13012023
# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count=0
        j=len(digits)-1
        for i in digits:
            if i == 9:
                count+=1
        if len(digits)==count:
            digits.append(0)
            digits[0]=1
            for i in range(1,len(digits)-1):
                digits[i]=0
        else:
            if j == 0:
                if digits[j]!=9:
                    digits[j]+=1
                else:
                    digits.append(0)
                    digits[0]=1
            while j>0:
                if digits[j]!=9:
                    digits[j]+=1
                    break
                while digits[j]==9:
                    digits[j] = 0
                    j-=1
                digits[j]+=1
                break
        return digits

        # for i in range(0,len(digits)):
        #     digits[i] = str(digits[i])
        # digits = "".join(digits)
        # digits = int(digits)
        # digits = digits + 1
        # digits = str(digits)
        # return ([int(x) for x in digits])
