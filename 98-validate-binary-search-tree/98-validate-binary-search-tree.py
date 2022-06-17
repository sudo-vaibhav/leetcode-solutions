class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root,maxi=inf,mini=-inf):
            if not root:return True
            cur = root.val
            return mini<cur<maxi and solve(root.left,min(maxi,cur),mini) and solve(root.right,maxi,max(mini,cur))        
        return solve(root)