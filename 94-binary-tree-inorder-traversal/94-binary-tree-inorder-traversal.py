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
                temp2 = temp.left
                while temp2.right and temp2.right!=temp:
                    temp2 = temp2.right
                
                if temp2.right==temp:
                    ans.append(temp.val)
                    temp2.next = None
                    temp = temp.right
                    
                else:
                    temp2.right = temp
                    temp = temp.left
        
        return ans
                    