# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast,prev = head,head,None

        if fast and fast.next:
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
        else:
            return fast
        
        if fast:
            temp = slow.next
            slow.next = None
            slow = temp
        else:
            prev.next = None
                
        def rev(node):
            prev = None
            while node.next:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            node.next = prev
            return node
            
        tail = rev(slow)
        backup = head # make a copy of head
        while tail:
            t = head.next
            head.next = tail
            t2 = tail.next
            tail.next = t
            head = t
            tail = t2
        return backup
            
            
        
        
        