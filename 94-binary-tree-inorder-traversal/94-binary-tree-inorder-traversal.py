# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        temp = root
        ans = []
        while temp:
            if not temp.left:
                ans.append(temp.val)
                temp = temp.right
            else:
                rightmostLeaf = temp.left
                while rightmostLeaf.right and rightmostLeaf.right!=temp:
                    rightmostLeaf = rightmostLeaf.right
                
                if rightmostLeaf.right==None:
                    rightmostLeaf.right = temp
                    temp = temp.left
                else:
                    ans.append(temp.val)
                    rightmostLeaf.right = None
                    temp = temp.right
        return ans