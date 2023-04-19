# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        nodes = []
        
        
        def lvr(node):
            if not node: return
            lvr(node.left)
            nodes.append(node)
            lvr(node.right)
        
        @cache
        def solve(node,prev):
            if not node: return 0
            if prev=="left":
                return 1+solve(node.right,"right")
            else:
                return 1+solve(node.left,"left")
            
            
        lvr(root)
        ans = 1
        for node in nodes:
            ans = max(ans,solve(node,"left"),solve(node,"right"))
        
        return ans-1