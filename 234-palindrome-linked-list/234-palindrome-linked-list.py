# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow,fast = head,head
        prev = None
        
#         if not head or not head.next:
#             return True
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        p1 = head
        if fast==None:
            # even length 
            p2 = slow
        else:
            # odd length
            p2 = slow.next
        
        def reverse(head):
            prev = None
            temp = head
            while temp:
                nex = temp.next
                temp.next = prev
                prev = temp
                temp = nex
            return prev
        
        # reverse second half and compare with first
        p2 = reverse(p2)
        while p1 and p2:
            if p1.val!=p2.val:
                return False
            p1,p2 = p1.next,p2.next
        return True