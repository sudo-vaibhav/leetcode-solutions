# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def lcaOrFind(root,p,q):
            if root==None or root==p or root==q:
                return root
            L = lcaOrFind(root.left,p,q)
            R = lcaOrFind(root.right,p,q)
            
            if L and R:
                return root
            else:
                return L or R
            
        
        return lcaOrFind(root,p,q)