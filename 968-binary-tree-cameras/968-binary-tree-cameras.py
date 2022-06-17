class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        @cache
        def solve(node,amMonitored,throughCur):
            if not node: return 0
            if amMonitored:
                if throughCur:
                    return solve(node.left,True,False)+solve(node.right,True,False)
                else:
                    return min(solve(node.left,False,False)+solve(node.right,False,False)
                               , 1+solve(node.left,True,False)+solve(node.right,True,False))
            else:
                # if not node.left and not node.right:
                #     return 1
                # else:
                return 1+min(solve(node.left,True,True)+solve(node.right,False,None),solve(node.left,False,None)+solve(node.right,True,True),solve(node.left,True,False)+solve(node.right,True,False))
        return solve(root,False,None)