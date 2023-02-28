# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        pat = defaultdict(list)
        ans = []
        def solve(root):
            if not root: return "None"
            p = str(root.val)+","+solve(root.left)+","+solve(root.right)
            pat[p].append(root)
            return p
            
        solve(root)
        
        for i in pat:
            if len(pat[i])>1:
                ans.append(pat[i][0])
        
        return ans