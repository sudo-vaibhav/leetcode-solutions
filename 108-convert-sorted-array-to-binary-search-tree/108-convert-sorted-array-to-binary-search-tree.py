# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def solve(l,r):
            if l<=r:
                m = (l+r)//2
                node = TreeNode(nums[m])
                node.left = solve(l,m-1)
                node.right = solve(m+1,r)
                return node
        return solve(0,len(nums)-1)