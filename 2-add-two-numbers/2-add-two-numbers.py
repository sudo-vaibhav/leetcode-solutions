# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        temp = dummy
        p1,p2,carry = l1,l2,0
        while p1 or p2:
            cur1,cur2 = p1.val if p1 else 0,p2.val if p2 else 0
            tot = cur1+cur2+carry
            curVal = tot%10
            node = ListNode(curVal)
            temp.next = node
            temp = temp.next
            if tot>=10:
                carry = 1
            else:
                carry = 0
            if p1: p1=p1.next
            if p2: p2=p2.next
        if carry:
            temp.next = ListNode(carry)
                
        return dummy.next