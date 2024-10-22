# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = defaultdict(int)
        def trav(node,lvl=0):
            nonlocal sums
            if not node:
                return
            sums[lvl]+= node.val
            trav(node.left,lvl+1)
            trav(node.right,lvl+1)
        trav(root)
        s = list(sorted(sums.values(),reverse=True))
        if len(s)<k:
            return -1
        return s[k-1]
            