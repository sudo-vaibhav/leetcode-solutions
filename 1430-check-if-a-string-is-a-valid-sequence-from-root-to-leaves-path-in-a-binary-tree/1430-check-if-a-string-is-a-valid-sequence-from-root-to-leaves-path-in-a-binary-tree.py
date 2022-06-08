# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        N = len(arr)
        
        
        def dfs(node,idx,prev=None):
            if idx==N:
                return node==None and prev.left==None and prev.right==None
            if node==None:
                return False
            else:
                if arr[idx]==node.val:
                    return dfs(node.left,idx+1,node) or dfs(node.right,idx+1,node)
                else:
                    return False
        
        return dfs(root,0)
        