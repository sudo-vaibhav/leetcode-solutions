# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        
        def solve(l,r):
            if l<=r:
                cur = preorder[l]
                toPlace = bisect_left(preorder,cur,l+1,r+1)
                node = TreeNode(cur)
                node.left = solve(l+1,toPlace-1)
                node.right = solve(toPlace,r)
                return node
        
        return solve(0,n-1)