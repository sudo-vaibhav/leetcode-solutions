# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def solve(node):
            if node:
                return solve(node.left)+solve(node.right)+(node.val if low<=node.val<=high else 0)
            return 0
                
        return solve(root)