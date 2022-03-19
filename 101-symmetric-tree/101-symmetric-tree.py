# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,r1,r2):
        if not r1 and not r2 : return True
        elif not r1 or not r2: return False
        else:
            return r1.val==r2.val and self.solve(r1.left,r2.right) and self.solve(r1.right,r2.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root : return True
        return self.solve(root.left,root.right)