# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        def solve(node,mi,ma):
            if node:
                return max(
                
                    abs(mi-node.val),abs(ma-node.val),
                    solve(node.left,min(mi,node.val),max(ma,node.val)),
                    solve(node.right,min(mi,node.val),max(ma,node.val))
                )
            return 0
        
        return max(solve(root.left,root.val,root.val),solve(root.right,root.val,root.val))