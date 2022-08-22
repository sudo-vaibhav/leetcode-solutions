# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 1
        inc,dec = 0,1
        def solve(root):
            nonlocal ans
            if not root: return (0,0)
            # if not root.left and not root.right: return (1,1)
            L,R = solve(root.left),solve(root.right)
            LInc = 1 if (L[inc]==0 or root.left.val!=root.val+1) else L[inc]+1
            LDec = 1 if (L[dec]==0 or root.left.val!=root.val-1) else L[dec]+1
            RInc = 1 if (R[inc]==0 or root.right.val!=root.val+1) else R[inc]+1
            RDec = 1 if (R[dec]==0 or root.right.val!=root.val-1) else R[dec]+1
            
            ans = max(ans,LInc+RDec-1,LDec+RInc-1)
            return (max(LInc,RInc),max(LDec,RDec))
        
        solve(root)
        
        return ans