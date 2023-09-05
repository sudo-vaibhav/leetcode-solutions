"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

def printlist(node):
    while node:
        print(node.val,node.random.val if node.random else None)
        node = node.next
    

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        temp,dummy = head,Node(0)
        
        while temp:
            new_node = Node(temp.val)
            actual_temp = temp.next
            # dummy = dummy.next
            temp.next = new_node
            new_node.next = actual_temp
            temp = actual_temp
        ans = head.next
        
        temp,temp2 = head,head.next
        # printlist(head)
        while temp:
            if temp.random:
                temp2.random = temp.random.next
            else:
                temp2.random = None
            temp = temp2.next
            if temp:
                temp2 = temp.next
            else:
                temp2 = None
        # return ans
        temp,temp2 = head,head.next
        # printlist(ans)
        while temp and temp2:
            temp.next = temp2.next
            if temp2.next:
                temp2.next = temp2.next.next
            else:
                temp2.next = None
            temp = temp.next
            temp2 = temp2.next
        return ans