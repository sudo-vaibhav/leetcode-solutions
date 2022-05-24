# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getMiddle(self,head):
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def reverse(self,head):
        prev,temp = None,head
        while temp:
            nex = temp.next
            temp.next = prev
            prev = temp
            temp = nex
        return prev
    
    def printList(self,head):
        pass
        
    def pairSum(self, head):
        middle = self.getMiddle(head)
        p1,p2 = head,self.reverse(middle)
        self.printList(p1)
        self.printList(p2)
        ans = -float("inf")
        while p1 and p2:
            ans = max(ans,p1.val+p2.val)
            p1,p2 = p1.next,p2.next
        return ans