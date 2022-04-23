# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right: return head
        temp = head
        prev = None
        nodeCount = 1
        while temp:
            if nodeCount==left:
                break
            prev = temp 
            temp = temp.next
            nodeCount+=1
        firstNode = temp
        
        nextNode = temp.next
        curNode = temp
        
        while nextNode and nodeCount!=right:
            nex = nextNode.next
            nextNode.next = curNode
            curNode = nextNode
            nextNode = nex
            nodeCount+=1
        if prev:
            prev.next = curNode
        firstNode.next = nextNode
        
        if prev==None:
            return curNode
        else:
            return head