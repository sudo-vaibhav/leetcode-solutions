# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder: return None
        rootValIdx = inorder.index(postorder[-1])
        leftTreeIO = inorder[:rootValIdx]
        rightTreeIO = inorder[rootValIdx+1:]
        # temp = 
        leftTreePO = postorder[:len(leftTreeIO)]
        rightTreePO = postorder[len(leftTreeIO):-1]
        return TreeNode(postorder[-1],self.buildTree(leftTreeIO,leftTreePO),self.buildTree(rightTreeIO,rightTreePO))