class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        temp = root
        while temp:
            self.st.append(temp)
            temp = temp.left
    def next(self) -> int:
        node = self.st.pop()
        v = node.val
        temp = node.right
        while temp:
            self.st.append(temp)
            temp = temp.left
        return v
    def hasNext(self) -> bool:
        return not not self.st
