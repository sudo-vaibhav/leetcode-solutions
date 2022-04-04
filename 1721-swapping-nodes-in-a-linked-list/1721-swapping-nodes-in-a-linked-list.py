# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k2=k
        t1=head
        while k2>1:
            t1 = t1.next
            k2-=1
        temp=t1
        t2=head
        while t1.next:
            t2=t2.next
            t1=t1.next
        tempval=temp.val
        temp.val=t2.val
        t2.val = tempval
        return head