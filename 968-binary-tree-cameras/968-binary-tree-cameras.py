class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        NotApplicable = None
        @cache
        def solve(node,amMonitored,monitoredThroughCur):
            if not node: return 0
            if amMonitored:
                if monitoredThroughCur:
                    return solve(node.left,True,False)+solve(node.right,True,False)
                else:
                    return min(solve(node.left,False,NotApplicable)+solve(node.right,False,NotApplicable)
                               , 1+solve(node.left,True,False)+solve(node.right,True,False))
            else:
                return 1+min(solve(node.left,True,True)+solve(node.right,False,NotApplicable),solve(node.left,False,NotApplicable)+solve(node.right,True,True),solve(node.left,True,False)+solve(node.right,True,False))
        
        return solve(root,False,NotApplicable)