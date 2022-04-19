# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def pl(head):
            return
            temp = head
            print("printing list")
            while temp:
                print(temp.val,end=",")
                temp=temp.next
            print()
            # print("length",self.length)
        # print(head)
        slow = head
        fast = head
        prev = None
        if fast and fast.next:
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
                
        else:
#             single length linked list
            return fast
        
        # print(prev)
        if fast:
            temp = slow.next
            slow.next = None
            slow = temp
            # prev = None
        else:
            prev.next = None
            # prev = None
        
        # pl(head)
        # pl(slow)
        
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
        # pl(head)
        # pl(tail)
        backup = head
        while tail:
            t = head.next
            head.next = tail
            t2 = tail.next
            tail.next = t
            head = t
            tail = t2
        return backup
            
            
        
        
        