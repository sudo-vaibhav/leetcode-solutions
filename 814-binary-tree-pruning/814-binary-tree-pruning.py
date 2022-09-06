# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def solve(root):
            if not root:return False
            L,R = solve(root.left),solve(root.right)
            if not L:
                root.left = None
            if not R:
                root.right = None
            return L or R or root.val==1
            
        ans = solve(root)
        if not ans:
            return None
        else:
            return root