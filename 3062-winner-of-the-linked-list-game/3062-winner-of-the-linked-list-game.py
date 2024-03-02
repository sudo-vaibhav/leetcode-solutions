# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        temp=head
        e,o = 0,0
        while temp and temp.next:
            evenVal = temp.val
            oddVal = temp.next.val
            if evenVal>oddVal:
                e+=1
            elif evenVal<oddVal:
                o+=1
            temp = temp.next.next
        
        if e==o:
            return "Tie"
        elif e>o:
            return "Even"
        return "Odd"