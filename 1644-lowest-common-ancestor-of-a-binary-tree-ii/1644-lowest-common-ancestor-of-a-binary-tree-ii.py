# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        anc = set()
        def populateAncestry(node):
            if node:
                if node.val==p.val:
                    anc.add(p.val)
                    return True
                else:
                    L,R = populateAncestry(node.left),populateAncestry(node.right)
                    if L or R:
                        anc.add(node.val)
                        return True
            return False
        
        populateAncestry(root)
        ans = None
        def find(node):
            nonlocal ans
            if node:
                if node.val==q.val:
                    if q.val in anc and ans==None:
                        ans = q
                    return True
                else:
                    L,R = find(node.left),find(node.right)
                    if L or R:
                        if node.val in anc and ans==None:
                            ans = node
                        return True
            return False
        find(root)
        return ans