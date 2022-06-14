# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def lvr(root):
            if not root:return (0,True)
            l = lvr(root.left)
            r = lvr(root.right)
            
            isBal =  l[1] and r[1] and abs(l[0]-r[0])<=1
            
            return (1+max(l[0],r[0]),isBal)
        
        return lvr(root)[1]