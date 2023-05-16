# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        if not temp : return head
        nex = temp.next
        
        while nex:
            temp.val,nex.val = nex.val,temp.val
            temp = temp.next.next
            nex = nex.next
            if nex:
                nex =nex.next
        return head