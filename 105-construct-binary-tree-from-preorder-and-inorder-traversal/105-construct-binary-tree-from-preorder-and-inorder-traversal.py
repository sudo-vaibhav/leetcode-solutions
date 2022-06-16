# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        
        def solve(idx,l,r):
            if l<=r and idx<n:
                cur = preorder[idx]
                node = TreeNode(cur)
                inorderIdx = None
                for i in range(l,r+1):
                    if inorder[i]==cur:
                        inorderIdx = i
                        break
                inLeftSubTree = inorderIdx-l
                node.left = solve(idx+1,l,inorderIdx-1)
                node.right = solve(idx+1+inLeftSubTree,inorderIdx+1,r)
                return node
        
        
        ans = solve(0,0,n-1)
        return ans