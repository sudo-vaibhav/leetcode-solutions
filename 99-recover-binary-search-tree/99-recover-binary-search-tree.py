# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
#         3 2 1
#         1 3 2 4

        def lvr(root):
            if not root: return []
            return [*lvr(root.left),root,*lvr(root.right)]
        
        trav = lvr(root)
        sted = sorted(trav,key=lambda x:x.val)
        viol1,viol2,n = inf,inf,len(trav)
        for i in range(n):
            if trav[i].val!=sted[i].val:
                if viol1==inf:
                    viol1=trav[i]
                else:
                    viol2=trav[i]
                    break
        viol1.val,viol2.val = viol2.val,viol1.val
        
        