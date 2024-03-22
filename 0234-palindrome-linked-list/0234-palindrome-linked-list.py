# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def findMid(head):
            slow,fast = head,head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow,fast==None
        
        mid,evenLen = findMid(head) 
        # stop = mid
        if not evenLen:
            mid = mid.next
        
        def reverse(head):
            temp = None
            while head:
                tmp = head.next
                head.next = temp
                temp = head
                head = tmp
            return temp
        newHead = reverse(mid)
        # print(newHead.val)
        while newHead:
            # print(newHead.val,head.val)
            if newHead.val!=head.val:
                return False
            newHead = newHead.next
            head = head.next
        return True