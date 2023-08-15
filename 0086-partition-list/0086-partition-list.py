# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p1,p2 = ListNode(),ListNode()
        
        t1,t2 = p1,p2
        
        temp = head
        while temp:
            if temp.val<x:
                t1.next = temp
                t1 = t1.next
            else:
                t2.next = temp
                t2 = t2.next
            temp = temp.next
        
        t1.next = p2.next
        t2.next = None
        
        return p1.next