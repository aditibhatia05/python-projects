# 14012023
# https://leetcode.com/problems/add-binary/description/

# Solution by applying logic of binary addition

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a=len(a)
        len_b=len(b)
        cf = 0
        result=""

        diff = abs(len_a-len_b)
        if len_a>len_b:
            b=b.rjust(diff+len(b),'0')
        else:
            a=a.rjust(diff+len(a),'0')
        print(a)
        print(b)
        i=len(a)-1
        while i >= 0:
            if a[i]=='1' and b[i]=='1':
                if cf==0:
                    result='0'+result
                    cf=1
                else:
                    result='1'+result
                    cf=1
            elif (a[i]=='1' and b[i]=='0') or (a[i]=='0' and b[i]=='1'):
                if cf==0:
                    result='1'+result
                    cf=0
                else:
                    result='0'+result
                    cf=1
            elif (a[i]=='0' and b[i]=='0'):
                if cf==1:
                    result='1'+result
                    cf=0
                else:
                    result='0'+result
                    cf=0
            i-=1
        if cf==1:
            result='1'+result
        return(result)




# Solution by converting first to decimal and then adding and then recoverting to binary

        # q = 0
        # w = len(a)-1
        # decimal_a = 0
        # for q in range(0,w+1):
        #     decimal_a+=(int(a[q])*(2**(w-q)))
        # e = 0
        # r = len(b)-1
        # decimal_b = 0
        # for e in range(0,r+1):
        #     decimal_b+=(int(b[e])*(2**(r-e)))
        # sum = decimal_a + decimal_b
        # result=""
        # while sum>1:
        #     if sum%2==0:
        #         result+='0'
        #     else:
        #         result+='1'
        #     sum=int(sum//2)
        # if sum==1:
        #     result+='1'
        # elif sum==0:
        #     result+='0'
        # result = result[::-1]
        # return result




        

        
