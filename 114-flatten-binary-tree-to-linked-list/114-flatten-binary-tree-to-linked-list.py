# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.prev = None    
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return root
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.left = None
        root.right = self.prev
        self.prev = root
        