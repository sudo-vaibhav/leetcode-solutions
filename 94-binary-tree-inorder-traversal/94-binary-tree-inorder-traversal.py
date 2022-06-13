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
                rightMostLeaf = temp.left
                while rightMostLeaf.right and rightMostLeaf.right!=temp:
                    rightMostLeaf = rightMostLeaf.right
                if rightMostLeaf.right==temp:
                    ans.append(temp.val)
                    rightMostLeaf.next = None
                    temp = temp.right
                else:
                    rightMostLeaf.right = temp
                    temp = temp.left
        return ans
                    