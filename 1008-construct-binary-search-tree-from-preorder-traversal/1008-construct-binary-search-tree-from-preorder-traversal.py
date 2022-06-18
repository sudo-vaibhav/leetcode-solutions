# class Solution:
#     def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
#         n = len(preorder)
#         def solve(l,r):
#             if l<=r:
#                 cur = preorder[l]
#                 toPlace = bisect_left(preorder,cur,l+1,r+1)
#                 node = TreeNode(cur)
#                 node.left = solve(l+1,toPlace-1)
#                 node.right = solve(toPlace,r)
#                 return node
#         return solve(0,n-1)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        idx=0
        
        def helper(upperBound=inf):
            nonlocal idx
            if idx==n or preorder[idx]>=upperBound:return None
            node = TreeNode(preorder[idx])
            idx+=1
            node.left = helper(node.val)
            node.right = helper(upperBound)
            return node
        return helper() 