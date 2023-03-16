# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
        d={}
        
        def clone(root):
            if not root:return None
            if root not in d:
                d[root]=NodeCopy(root.val)
                d[root].left = clone(root.left)
                d[root].right = clone(root.right)
                d[root].random = clone(root.random)
            #     retur
            # else:
            return d[root]
            
        
            
        return clone(root)