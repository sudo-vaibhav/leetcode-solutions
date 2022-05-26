# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head or not head.next: return head
        d1,d2 = ListNode(),ListNode()
        h1,h2 = d1,d2
        
        temp = head
        lastOfLeft = None
        while temp:
            v = temp.val
            if v<x:
                d1.next = temp
                d1 = temp
                lastOfLeft = temp
            else:
                d2.next = temp
                d2 = temp
            t = temp.next
            temp.next = None
            temp = t
        if not lastOfLeft:return h2.next
        lastOfLeft.next = h2.next
        return h1.next
        