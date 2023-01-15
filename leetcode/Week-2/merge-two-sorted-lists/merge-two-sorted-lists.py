# 15012023
# https://leetcode.com/problems/merge-two-sorted-lists/

#two lists:

class Solution:
    def mergeTwoLists(self, list1, list2):
        i=0
        j=0
        k=0
        list3 = []
        while list1 and list2:
            if list1[i] < list2[j]:
                list3.append(list1[i])
                k+=1
                list1.pop(i)
            else:
                list3.append(list2[j])
                k+=1
                list2.pop(j)
        if list1:
            for ele in list1:
                list3.append(ele)                    
        elif list2:
            for ele in list2:
                list3.append(ele) 
        return list3
       
s1 = Solution()
output = s1.mergeTwoLists([],[1])
print(output)


#two linked lists

class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         tempHead = ListNode()
#         list3Head = tempHead
#         while list1 and list2:
#             if list1.val < list2.val:
#                 tempHead.next = list1
#                 list1 = list1.next
#             else:
#                 tempHead.next = list2
#                 list2 = list2.next
#             tempHead = tempHead.next
        
#         if list1:
#             tempHead.next = list1
#         elif list2:
#             tempHead.next = list2
#         return list3Head.next