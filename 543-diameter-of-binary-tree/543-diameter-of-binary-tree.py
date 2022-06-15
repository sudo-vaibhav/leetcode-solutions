# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def solve(node):
            nonlocal ans
            if not node: return 0
            L,R = solve(node.left),solve(node.right)
            ans = max(ans,1+L+R)
            return 1+max(L,R)
        
        solve(root)
        return ans-1
        