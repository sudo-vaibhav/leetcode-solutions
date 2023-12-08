# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        ans = 0
            
        def solve(node):
            if not node: return (0,0)
            nonlocal ans
            L,R = solve(node.left),solve(node.right)
            t1,t2 = (L[0]+R[0]+node.val),(L[1]+R[1]+1)
            ans = max(ans,t1/t2)
            return (t1,t2)
        
        solve(root)
        return ans
        