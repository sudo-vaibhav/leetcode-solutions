# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        @cache
        def solve(node,canPickSelf):
            if node:
    #             you can always choose to not pick yourself
                notPickSelf = solve(node.left,True)+solve(node.right,True)

                pickSelf = 0    
                if canPickSelf:
                    pickSelf = node.val+solve(node.left,False)+solve(node.right,False)

                return max(notPickSelf,pickSelf)
            return 0
        
        return solve(root,True)