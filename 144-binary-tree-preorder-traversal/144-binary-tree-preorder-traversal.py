# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        def vlr(root):
            if not root: return
            ans.append(root.val)
            vlr(root.left)
            vlr(root.right)
        
        vlr(root)
        return ans
        
        
        