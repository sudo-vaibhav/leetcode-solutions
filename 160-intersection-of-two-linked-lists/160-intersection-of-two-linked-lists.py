# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        t1,t2 = headA,headB
        
        while t1 and t2:
            t1 = t1.next
            t2 = t2.next
            
        if t1==None:
            t1 = headB
            backup = headA
        else:
            t2 = headA
            backup = headB
        
        while t1 and t2:
            t1 = t1.next
            t2 = t2.next
            
        if t1==None:
            t1 = backup
        else:
            t2 = backup
        
        while t1 and t2:
            if t1==t2: return t1
            t1 = t1.next
            t2 = t2.next
        
        return None
            