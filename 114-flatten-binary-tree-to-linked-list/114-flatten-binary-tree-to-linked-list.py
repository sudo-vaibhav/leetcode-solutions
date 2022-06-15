class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        prev = None
        
        def vlr(node):
            nonlocal prev
            if not node: return
            L,R = node.left,node.right
            if prev:
                prev.right = node
            prev = node
            node.left = None
            vlr(L)
            vlr(R)

        vlr(root)
