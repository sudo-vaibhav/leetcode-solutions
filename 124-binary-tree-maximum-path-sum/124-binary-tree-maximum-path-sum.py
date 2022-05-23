# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if not root: return 0
        else:
            L = self.solve(root.left)
            R = self.solve(root.right)
            self.ans = max(self.ans,root.val+max(0,L)+max(0,R))
            
            return root.val+max(0,L,R)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        self.solve(root)
        return self.ans