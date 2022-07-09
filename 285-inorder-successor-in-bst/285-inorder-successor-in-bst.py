# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        prev = None
        ans = None
        def lvr(node):
            nonlocal ans,prev
            if not node: return
            lvr(node.left)
            if prev and prev==p:
                ans = node
            prev = node 
            lvr(node.right)
        
        lvr(root)
        
        return ans