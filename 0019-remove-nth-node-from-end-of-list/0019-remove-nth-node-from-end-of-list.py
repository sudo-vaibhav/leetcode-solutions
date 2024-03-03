# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy, temp = head,head
        if not head.next:
            return None
        while n>0:
            temp = temp.next
            n-=1
        try:
            while temp.next:
                temp = temp.next
                dummy = dummy.next
        except:
            return head.next
        dummy.next = dummy.next.next
        return head