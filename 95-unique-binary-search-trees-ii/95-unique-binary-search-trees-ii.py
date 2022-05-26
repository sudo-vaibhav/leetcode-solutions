# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        i = 1
        nums = list()
        while i<=n:
            nums.append(i)
            i+=1
        print(nums)
        
        
        def solve(arr):
            if len(arr)==0: return [None]
            ans = []
            for idx in range(len(arr)):
                L = solve(arr[:idx])
                R = solve(arr[idx+1:])
                for l in L:
                    for r in R:
                        ans.append(TreeNode(arr[idx],l,r))
            return ans
        
        return solve(nums)