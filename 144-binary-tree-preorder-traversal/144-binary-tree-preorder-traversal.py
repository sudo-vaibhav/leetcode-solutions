# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         ans = []
#         def vlr(root):
#             if not root: return
#             ans.append(root.val)
#             vlr(root.left)
#             vlr(root.right)
        
#         vlr(root)
#         return ans
        
#         vlr
        temp = root
        ans = []
        
        while temp:
            if not temp.left:
                ans.append(temp.val)
                temp = temp.right
            else:
                leftmostLeaf = temp.left
                while leftmostLeaf.right and leftmostLeaf.right!=temp:
                    leftmostLeaf = leftmostLeaf.right
                
                if leftmostLeaf.right==None:
                    ans.append(temp.val)
                    leftmostLeaf.right = temp
                    temp = temp.left
                else:
                    leftmostLeaf.right = None
                    temp = temp.right
        return ans
        
        