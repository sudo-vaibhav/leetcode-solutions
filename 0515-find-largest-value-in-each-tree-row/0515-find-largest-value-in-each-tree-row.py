# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(lambda : -inf)
        
        def solve(node,level=0):
            if node:
                ans[level]=max(ans[level],node.val)
                solve(node.left,level+1)
                solve(node.right,level+1)
        solve(root)
        return map(lambda x:x[1],sorted(ans.items()))