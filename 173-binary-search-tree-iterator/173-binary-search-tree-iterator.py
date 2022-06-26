# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = [root]
        temp = root
        while temp.left:
            self.st.append(temp.left)
            temp = temp.left
        
    def next(self) -> int:
        node = self.st.pop()
        v = node.val
        right = node.right
        if right:
            self.st.append(right)
            while right.left:
                self.st.append(right.left)
                right = right.left
        return v
        

    def hasNext(self) -> bool:
        return not not self.st


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()