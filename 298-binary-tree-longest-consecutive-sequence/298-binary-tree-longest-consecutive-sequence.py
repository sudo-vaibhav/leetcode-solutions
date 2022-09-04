# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        
        ans = 1
        
        def solve(root):
            nonlocal ans
            if root:
                curAns = 1
                R = solve(root.right)
                L = solve(root.left)
                if root.right and root.right.val==root.val+1:
                    curAns = R+1
                if root.left and root.left.val == root.val+1:
                    curAns = max(curAns,L+1)
                ans = max(ans,curAns)
                return curAns
            return 0
                
            
        solve(root)
        return ans