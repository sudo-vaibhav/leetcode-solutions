class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        prev,ans = None,None
        def lvr(root):
            nonlocal prev,ans
            if not root: return
            lvr(root.left)
            if prev:
                prev.right = root
            else :
                ans = root
            prev = root
            root.left=None
            lvr(root.right)
        lvr(root)
        return ans
        
        
        
                