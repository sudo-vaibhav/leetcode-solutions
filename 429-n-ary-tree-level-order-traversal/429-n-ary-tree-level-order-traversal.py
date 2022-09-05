"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        q = deque()
        ans = []
        if root:
            q.append(root)
            while q:
                lenQ = len(q)
                temp = []
                for _ in range(lenQ):
                    cur = q.popleft()
                    temp.append(cur.val)
                    for c in cur.children:
                        q.append(c)
                ans.append(temp)
        return ans