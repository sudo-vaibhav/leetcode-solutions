# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def solve(n):
            if n==1: return [TreeNode(0)]
            ans = []
            for on_left in range(1,n-1):
                on_right = n-1-on_left
                left_possibilities = solve(on_left)
                right_possibilities = solve(on_right)
                for left_pos in left_possibilities:
                    for right_pos in right_possibilities:
                        ans.append(TreeNode(0,left_pos,right_pos))
            return ans
        
        return solve(n)