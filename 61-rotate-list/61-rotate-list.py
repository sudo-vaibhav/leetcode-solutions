# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0: return head
        lastNode,n = head,1
        while lastNode.next:
            lastNode,n = lastNode.next,n+1
        lastNode.next = head
        k%=n
        keepFromBegin = n-k
        while keepFromBegin:
            lastNode,keepFromBegin = lastNode.next, keepFromBegin-1
        newHead = lastNode.next
        lastNode.next = None
        return newHead
        
        
        