# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def solve(node):
            nonlocal ans
            if node:
                ls,lc = solve(node.left)
                rs,rc = solve(node.right)
                ts,tc = ls+rs+node.val,lc+rc+1
                ans += int(node.val==(ts)//(tc))
                return (ts,tc)
            return (0,0)
        solve(root)
        return ans