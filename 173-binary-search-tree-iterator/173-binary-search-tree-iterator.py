class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        temp = root
        while temp:
            self.st.append(temp)
            temp = temp.left
    def next(self) -> int:
        node = self.st.pop()
        temp = node.right
        while temp:
            self.st.append(temp)
            temp = temp.left
        return node.val
    def hasNext(self) -> bool:
        return self.st
