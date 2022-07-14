# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = defaultdict(list)
        
        def lvr(node):
            if not node:return 0
            v = max(lvr(node.left),lvr(node.right))
            ans[v].append(node.val)
            return v+1
        lvr(root)
        keys = sorted(list(ans.keys()))
        res = []
        for k in keys:
            res.append(ans[k])
            
        return res
        