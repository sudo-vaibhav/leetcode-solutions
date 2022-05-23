# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        p1,p2 = head,head
        
        while n:
            p2 = p2.next
            n-=1
        
        if not p2:
            return head.next
        
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        
        p1.next = p1.next.next
        return head
        