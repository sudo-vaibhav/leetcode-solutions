# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isMatch(self, s, t):
    #     if not(s and t):
    #         return s is t
    #     return (s.val == t.val and 
    #             self.isMatch(s.left, t.left) and 
    #             self.isMatch(s.right, t.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def isSame(n1,n2):
            if not (n1 and n2):
                return n1 is n2
            return n1.val==n2.val and isSame(n1.left,n2.left) and isSame(n1.right,n2.right)
        
        def solve(root,subroot):
            if isSame(root,subroot):
                return True
            if not root:
                return False
            return  solve(root.left,subroot) or solve(root.right,subroot)
            
        
        return solve(root,subRoot)
        # if self.isMatch(s, t): return True
        # if not s: return False
        # return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)