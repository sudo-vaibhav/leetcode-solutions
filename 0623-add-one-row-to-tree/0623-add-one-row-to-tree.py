# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            return TreeNode(val,root)
        def solve(cur,curDepth):
            if curDepth==depth-1:
                # if cur.left:
                cur.left = TreeNode(val,cur.left,None)
                cur.right = TreeNode(val,None,cur.right)
                return cur
            else:
                if cur.left:
                    cur.left = solve(cur.left,curDepth+1)
                if cur.right:
                    cur.right = solve(cur.right,curDepth+1)
                return cur
        
        return solve(root,1)