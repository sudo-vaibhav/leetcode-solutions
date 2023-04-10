# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff,ans = inf,None
        def solve(cur):
            nonlocal diff,ans
            if cur:
                v = cur.val
                temp = abs(v-target)
                if temp<diff:
                    diff = abs(v-target)
                    ans = v
                elif temp==diff:
                    ans = min(ans,v)
                solve(cur.left)
                solve(cur.right)
        solve(root)
        return ans
                
#         while cur:
#             v = cur.val
#             if abs(v-target)<diff:
                
#                 diff = abs(v-target)