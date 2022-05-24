# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow,fast=  head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                break
        else:
            return False
        return True
        