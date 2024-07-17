# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_d = set(to_delete)
        def solve(node):
            if not node:
                return
            node.left = solve(node.left)
            node.right = solve(node.right)
            
            if node.val in to_d:
                ans.append(node.left)
                ans.append(node.right)
                return None
            return node
            
        ans.append(solve(root))
        
        return filter(lambda x:x!=None,ans)