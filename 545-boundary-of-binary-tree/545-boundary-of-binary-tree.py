class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def isLeaf(node):
            return node and not(node.right or node.left)
        def leftBound(node):
            res = []
            while node and not isLeaf(node):
                res.append(node.val)
                node = node.left or node.right
            return res
        def rightBound(node):
            res = []
            while node and not isLeaf(node):
                res.append(node.val)
                node = node.right or node.left
            return res
        def getLeaves(node,leaves):
            if not node: return 
            if isLeaf(node):
                leaves.append(node.val)
            getLeaves(node.left,leaves)
            getLeaves(node.right,leaves)
        ans = [root.val]
        if isLeaf(root): return ans
        else:
            ans.extend(leftBound(root.left))
            leaves = []
            getLeaves(root,leaves)
            ans.extend(leaves)
            ans.extend(rightBound(root.right)[::-1],)
            return ans