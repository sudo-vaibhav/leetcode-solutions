# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
#         isBST, minVal, maxVal, sum
        def solve(node):
            nonlocal ans
            if not node:
                return (True,inf,-inf,0)
            # if not node.left and not node.right: 
            #     return (True,node.val,node.val,node.val)
            L = solve(node.left)
            R = solve(node.right)
            if L[0] and R[0] and L[2]<node.val<R[1]:
                tempSum = L[3]+R[3]+node.val
                ans = max(ans,tempSum)
                return (True,min(node.val,L[1],R[1]),max(node.val,L[2],R[2]),tempSum)
            return tuple([False])
        
        solve(root)
        return ans