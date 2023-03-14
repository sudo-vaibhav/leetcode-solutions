# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def solve(root,num=0):
            nonlocal ans
            if not root.left and not root.right: 
                # print(num)
                ans+=num*10+root.val
                return
            if root.left:
                solve(root.left,num*10+root.val)
            if root.right:
                solve(root.right,num*10+root.val)
        solve(root)
        return ans
            