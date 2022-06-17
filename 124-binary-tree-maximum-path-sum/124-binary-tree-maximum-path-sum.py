# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def solve(node):
            nonlocal ans
            if not node:return 0
            L,R = solve(node.left),solve(node.right)
            ans = max(ans,node.val+max(0,L)+max(0,R))
            return max(0,node.val,node.val+L,node.val+R)
        solve(root)
        return ans