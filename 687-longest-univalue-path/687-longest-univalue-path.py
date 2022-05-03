# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        ans = 1
        
        def dfs(root):
            nonlocal ans
            if not root.left and not root.right: return (root.val,1)
            
            # include root
            l = 0
            if root.left:
                temp = dfs(root.left)
                if root.val == temp[0]:
                    l = temp[1]
                    
            r = 0
            if root.right:
                temp = dfs(root.right)
                if root.val == temp[0]:
                    r = temp[1]
            
            # temp1 = (root.val,1+l+r)
            
            ans = max(ans,1+l+r)
            
            return (root.val,max(1+l,1+r))
                
                
        
        dfs(root)
        
        return ans-1