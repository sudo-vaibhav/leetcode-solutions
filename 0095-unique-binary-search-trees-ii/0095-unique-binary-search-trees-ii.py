# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # ans = []
        temp = TreeNode()
        
        @cache
        def solve(i,mini,maxi):
            if i==0:
                return [None]
            ans = []
            
            for onleft in range(0,i):
                temp = TreeNode(mini+onleft)
                onright = i-onleft-1
                L,R = solve(onleft,mini,mini+onleft-1),solve(onright,mini+onleft+1,maxi)
                for l in L:
                    for r in R:
                        temp.left = l
                        temp.right = r
                        ans.append(deepcopy(temp))
            return ans
        return solve(n,1,n)