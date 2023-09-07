# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        L,R = left,right
        if left==right: return head
        
        temp = head
        right-=left
        prev = None
        while left>1:
            prev = temp
            temp = temp.next
            left-=1
        ref1 = temp
        while right>0:
            temp = temp.next
            right-=1
        
        ref2 = temp
        # print(ref1.val,ref2.val,prev.val)
        dummy = ref1.next
        dummy2 = ref1
        
        while dummy and dummy!=ref2:
            nex = dummy.next
            dummy.next = dummy2
            dummy2 = dummy
            dummy = nex
        if dummy:
            ref1.next = dummy.next
            nex = dummy.next
            dummy.next = dummy2
            dummy2 = dummy
            dummy = nex
        if prev:
            prev.next = ref2
        # print(ref2)
        return head if L!=1 else ref2
        