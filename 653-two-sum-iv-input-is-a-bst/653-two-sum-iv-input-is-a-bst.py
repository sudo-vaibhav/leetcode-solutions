class BSTIterator:
    def __init__(self, root: Optional[TreeNode],traversal):
        self.st = []
        self.trav = traversal
        temp = root
        while temp:
            self.st.append(temp)
            temp = temp.left if self.trav=="lvr" else temp.right
    def peek(self):
        return self.st[-1].val
    def next(self) -> int:
        node = self.st.pop()
        temp = node.right if self.trav=="lvr" else node.left
        while temp:
            self.st.append(temp)
            temp = temp.left if self.trav=="lvr" else temp.right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l,r = BSTIterator(root,"lvr"),BSTIterator(root,"rvl")      
        while True:
            L,R = l.peek(),r.peek()
            if L>=R:break
            temp = L+R
            if temp==k: return True
            elif temp<k: l.next()
            else: r.next()
        return False