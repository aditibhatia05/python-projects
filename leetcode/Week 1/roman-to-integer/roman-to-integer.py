# 03012023
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        j= 0
        i = len(s)-1
        while(i>=j):
            if s[i]=='I':
                integer = integer + 1
                i = i - 1
            elif s[i]=='V':
                integer = integer + 5
                if s[i-1] == 'I':
                    if i-1<0: 
                        i = i - 1
                        continue
                    integer = integer - 1
                    i = i - 2
                    continue
                i = i - 1
            elif s[i]=='X':
                integer = integer + 10
                if s[i-1] == 'I':
                    if i-1<0: 
                        i = i - 1
                        continue
                    integer = integer - 1
                    i = i - 2
                    continue
                i = i - 1
            elif s[i]=='L':
                integer = integer + 50
                if s[i-1] == 'X':
                    if i-1<0: 
                        i = i - 1
                        continue
                    integer = integer - 10
                    i = i - 2
                    continue
                i = i - 1
            elif s[i]=='C':
                integer = integer + 100
                if s[i-1] == 'X':
                    if i-1<0: 
                        i = i - 1
                        continue
                    integer = integer - 10
                    i = i - 2
                    continue
                i = i - 1
            elif s[i]=='D':
                integer = integer + 500
                if s[i-1] == 'C':
                    if i-1<0: 
                        i = i - 1
                        continue  
                    integer = integer - 100
                    i = i - 2
                    continue
                i = i - 1
            elif s[i]=='M':
                integer = integer + 1000
                if s[i-1] == 'C':
                    if i-1<0: 
                        i = i - 1
                        continue
                    integer = integer - 100
                    i = i - 2
                    continue
                i = i - 1
        return integer
