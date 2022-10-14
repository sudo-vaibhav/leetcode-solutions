# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head
        prevSlow = None
        while fast and fast.next:
            fast = fast.next.next
            prevSlow = slow
            slow = slow.next
        
        if prevSlow:
            prevSlow.next = prevSlow.next.next
        else:
            return prevSlow
        # print(prevSlow)
        return head