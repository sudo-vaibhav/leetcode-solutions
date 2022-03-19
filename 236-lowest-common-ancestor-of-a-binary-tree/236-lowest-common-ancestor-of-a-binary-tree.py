# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        @cache
        def isIn(root,val):
            if not root : return False
            return root==val or isIn(root.left,val) or isIn(root.right,val)
        def solve(root,p,q):
            # print(root.val)
            if root == p or root== q : return root
            lp = isIn(root.left,p)
            lq = isIn(root.left,q)
            rp = isIn(root.right,p)
            rq = isIn(root.right,q)
            if((lp and rq)or(lq and rp)): return root
            else:
                if lp and lq: return solve(root.left,p,q)
                else: return solve(root.right,p,q)
        
        return solve(root,p,q)