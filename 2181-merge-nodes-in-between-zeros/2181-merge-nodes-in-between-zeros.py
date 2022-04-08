# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ans = dummy
        prev=0
        t = head.next
        while t:
            if t.val==0:
                ans.next = ListNode(prev)
                ans = ans.next
                prev = 0
            else:
                prev+=t.val
            t = t.next
        return dummy.next