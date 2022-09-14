# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def traverse(root,digitMask=0):
            if not root:return
            digitMask ^= 1<<root.val
            if not root.left and not root.right: self.res+=(digitMask&(digitMask-1)==0)
            else:
                traverse(root.left,digitMask)
                traverse(root.right,digitMask)
        traverse(root)
        return self.res
            