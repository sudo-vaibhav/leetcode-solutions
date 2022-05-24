# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,head,end):
            prev = None
            temp = head
            while temp and temp!=end:
                nex = temp.next
                temp.next = prev
                prev = temp
                temp = nex
            return prev
    def reverseKGroup(self, head, k):
        r = head
        l = head
        cnt = 0
        ans = None
        prev = None
        # while r:
        while r and cnt<k:
            prev = r
            r = r.next        
            cnt+=1
        if cnt!=k:
            return head

        newHead = self.reverse(l,r)
        if not ans:
            ans = newHead
        l.next = self.reverseKGroup(r,k)
        cnt=0
        
        return ans