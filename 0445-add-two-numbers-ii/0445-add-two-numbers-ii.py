# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getLen(node):
            if not node: return 0
            return 1+getLen(node.next)
        
        n1,n2 = getLen(l1),getLen(l2)
        
        n1,n2 = -n1,-n2
        
        
        def solve(node1,node2,i1,i2):
            if i1==0 and i2==0:
                return 0,None
            if i1==i2:
                carry,L = solve(node1.next,node2.next,i1+1,i2+1)
                val = node1.val+node2.val+carry
                return (val//10,ListNode(val%10,L))
            elif i1<i2:
                carry,L = solve(node1.next,node2,i1+1,i2)
                val = node1.val+carry
                return (val//10,ListNode(val%10,L))
            else:
                carry,L = solve(node1,node2.next,i1,i2+1)
                val = node2.val+carry
                return (val//10,ListNode(val%10,L))
                
                    
        carry,L = solve(l1,l2,n1,n2)
        if carry:
            return ListNode(carry,L)
        else:
            return L
            
        