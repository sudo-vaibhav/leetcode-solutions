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
        l,r = head,head
        ans,prevStepLastNode = None,None
        while r:
            cnt = 0
            while r and cnt<k:
                r,cnt = r.next,cnt+1        

            if cnt!=k:
                if prevStepLastNode:
                    prevStepLastNode.next = l
                    return ans
                else:
                    return head
            else:
                newHead = self.reverse(l,r)
                if prevStepLastNode:
                    prevStepLastNode.next = newHead
                else:
                    ans = newHead # no prev step means answer wont be defined already
                prevStepLastNode = l
            l = r # L is assigned to R, since sublist needs to be repopulated for next step
        return ans