# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         lvr
        ct = 0
        
        temp = root
        while temp:
            if not temp.left:
                ct+=1
                if ct==k:
                    return temp.val
                temp = temp.right
            else:
                rightMost = temp.left
                while rightMost.right and rightMost.right != temp:
                    rightMost = rightMost.right
                
                if rightMost.right==None:
                    rightMost.right = temp
                    temp = temp.left
                else:
                    rightMost.right = None
                    ct+=1
                    if ct==k:return temp.val
                    temp = temp.right
        return inf
                