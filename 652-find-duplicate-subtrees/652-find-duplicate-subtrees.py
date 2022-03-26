# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        s = defaultdict(list)
        def vlr(root:Optional[TreeNode])->str:
            if not root: return "#"
            curHash = str(root.val)+","+vlr(root.left)+","+vlr(root.right)
            s[curHash].append(root)
            return curHash
        vlr(root)
        return [s[h][0] for h in s.keys() if len(s[h])>1]
        