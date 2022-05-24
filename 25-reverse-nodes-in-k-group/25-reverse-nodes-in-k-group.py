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
        prevStep = None
        while r:
            while r and cnt<k:
                prev = r
                r = r.next        
                cnt+=1
            if cnt!=k:
                if prevStep:
                    prevStep.next = l
                else:
                    return head
                # pass
                # return head
            else:
                newHead = self.reverse(l,r)
                if prevStep:
                    prevStep.next = newHead
                else:
                    ans = newHead
                prevStep = l
            l = r
            cnt = 0
            
        # l.next = self.reverseKGroup(r,k)        
        return ans