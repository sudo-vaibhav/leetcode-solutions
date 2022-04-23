# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right: return head
        
        temp = head
        first = None
        prev = None
        i=1
        while temp:
            if i==left:
                first = temp
                break
            prev = temp 
            temp = temp.next
            i+=1
        
        # if first==None:
        #     return self.reverseBetween(head,head.val,prev.val)
        
        other = right
        
        fn = temp
        
        y = temp.next
        j = temp
        
        while y and i!=right:
            nex = y.next
            y.next = j
            j = y
            y = nex
            i+=1
        if prev:
            prev.next = j
        fn.next = y
        # print(prev)
        # print(y,prev)
#         while True:
#             nex = temp.next
#             backup = nex.next
#             nex.next = temp
            
#             if temp.val==other:
#                 otherNode = temp
#                 break
        # print(temp)
        # return None
        if prev==None:
            return j
        else:
            return head