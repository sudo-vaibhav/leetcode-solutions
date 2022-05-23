# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1: return list2
        if not list2: return list1
        
        if list1.val<=list2.val:
            temp = self.mergeTwoLists(list1.next,list2)
            head = list1
        else:
            temp = self.mergeTwoLists(list1,list2.next)
            head = list2
        
        head.next = temp
        return head