# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev,self.ans = inf,inf
        def solve(root):
            if not root: return
            solve(root.left)
            self.ans = min(self.ans,abs(self.prev-root.val))
            self.prev = root.val
            solve(root.right)
        solve(root)
        return self.ans