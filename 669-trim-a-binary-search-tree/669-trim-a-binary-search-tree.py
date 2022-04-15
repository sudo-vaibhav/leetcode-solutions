# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], lo: int, hi: int) -> Optional[TreeNode]:
        if not root: return root
        if root.val<lo:return self.trimBST(root.right,lo,hi)
        if root.val>hi:return self.trimBST(root.left,lo,hi)
        root.left=self.trimBST(root.left,lo,hi)
        root.right=self.trimBST(root.right,lo,hi)
        return root