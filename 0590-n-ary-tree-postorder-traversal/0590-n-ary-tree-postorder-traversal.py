"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def solve(node):
            if node:
                for c in node.children:
                    solve(c)
                ans.append(node.val)
        solve(root)
        return ans