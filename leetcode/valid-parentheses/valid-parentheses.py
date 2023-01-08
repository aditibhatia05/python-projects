


class Solution:
    def isValid(self, str: str) -> bool:
        counter1 = 0
        counter2 = 0
        counter3 = 0
        temp=[]
        for i in range(0, len(str)):
            if str[i]=="(":
                counter1+=1
                temp.append(str[i])
            elif str[i]=="{":
                counter2+=1
                temp.append(str[i])
            elif str[i]=="[":
                counter3+=1
                temp.append(str[i])
            elif str[i]==")":
                if counter1>=1 and temp[-1]=="(":
                    counter1-=1
                    temp.pop()
                else:
                    return False
            elif str[i]=="}":
                if counter2>=1 and temp[-1]=="{":
                    counter2-=1
                    temp.pop()
                else:
                    return False
            elif str[i]=="]":
                if counter3>=1 and temp[-1]=="[":
                    counter3-=1
                    temp.pop()
                else:
                    return False
        if temp==[]:
            return True
        else: return False



# Mohit's Solution
# class Solution:
# 
#     def isValid(self, s: str) -> bool:
#         d = {'(': ")", '[': "]", '{': "}"}
#         arr = []
#         for i in s:
#             if i in d:
#                 arr.append(i)
#             elif (i in d.values() and len(arr) != 0):
#                 for key, value in d.items():
#                     if value == i:
#                         keyInD = key
#                 if (arr[-1] == keyInD):
#                     arr.pop()
#                 else:
#                     return False
#             elif (i in d.values() and len(arr) == 0):
#                 return False
#         if len(arr) == 0:
#             return True
#         else:
#             return False
