# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        while temp and temp.next:
            num1,num2 = temp.val, temp.next.val
            gcdNode = ListNode(gcd(num1,num2),temp.next)
            temp.next = gcdNode
            temp = temp.next.next
        return head