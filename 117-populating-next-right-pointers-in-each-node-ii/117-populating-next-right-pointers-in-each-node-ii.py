"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        q.append(root)
        if not root: return root
        while q:
            qsize = len(q)
            for i in range(qsize):
                cur = q.popleft()
                if i==qsize-1:
                    cur.next = None
                else:
                    cur.next = q[0]
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root