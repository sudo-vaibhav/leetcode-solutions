# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        seen = set()
        
        temp = headA
        while temp:
            seen.add(temp)
            temp = temp.next
        
        temp = headB
        
        while temp:
            if temp in seen:
                return temp
            else:
                temp = temp.next
        
        return None