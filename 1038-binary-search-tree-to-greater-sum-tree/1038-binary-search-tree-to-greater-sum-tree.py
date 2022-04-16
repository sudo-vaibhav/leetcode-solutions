# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nodes = {}
        def lvr(root):
            if not root: return []
            nodes[root.val]=root
            return [*lvr(root.left),root.val,*lvr(root.right)]
    
        nodesList = lvr(root)
        s = sum(nodesList)
        curSum = 0
        for idx,node in enumerate(nodesList):
            curSum+=node
            nodes[node].val+=s-curSum
        return root