# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def solve(node,prev):
            # if not node.left and not node.right:
            if prev and ((prev.left==None) ^ (prev.right==None)):
                ans.append(node.val)
            # else:
            if node.left:
                solve(node.left,node)
            if node.right:
                solve(node.right,node)
        solve(root,None)
        return ans