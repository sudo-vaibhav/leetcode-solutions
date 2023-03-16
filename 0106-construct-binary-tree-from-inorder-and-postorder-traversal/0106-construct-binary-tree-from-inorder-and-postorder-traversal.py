# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        indices = {}
        for idx, i in enumerate(inorder):
            indices[i]=idx
            
        def solve(il,ir,pl,pr):
            if il>ir: return None
            rootVal = postorder[pr]
            rootPos = indices[rootVal]
            root = TreeNode(rootVal)
            countOnLeft = rootPos-il
            root.left = solve(il,rootPos-1,pl,pl+countOnLeft-1)
            root.right = solve(rootPos+1,ir,pl+countOnLeft,pr-1)
            return root
        
        return solve(0,n-1,0,n-1)
            