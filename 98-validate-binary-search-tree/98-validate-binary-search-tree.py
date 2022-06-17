# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def solve(root,maxi=inf,mini=-inf):
            if not root:return True
            cur = root.val
            if not (mini<cur<maxi): return False
            
            return solve(root.left,min(maxi,cur),mini) and solve(root.right,maxi,max(mini,cur))
        
        return solve(root)