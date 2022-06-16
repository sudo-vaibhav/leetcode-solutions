# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []
        
        def solve(node):
            if not node: return
            solve(node.left)
            solve(node.right)
            node.left = None
            node.right = None
            vals.append(node)
        solve(root)
        vals.sort(key=lambda x:x.val)
        # print(vals)
        def populate(l,r):
            if l<=r:
                mid = l+(r-l)//2
                vals[mid].left = populate(l,mid-1)
                vals[mid].right = populate(mid+1,r)
                return vals[mid] 
        
        return populate(0,len(vals)-1)