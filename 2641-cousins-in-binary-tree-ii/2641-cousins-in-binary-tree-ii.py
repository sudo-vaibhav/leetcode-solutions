# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lvlSum = defaultdict(int)
        childSumMap = {}
        def popLevelSums(node,lvl=0):
            if node:
                lvlSum[lvl]+=node.val
                popLevelSums(node.left,lvl+1)
                popLevelSums(node.right,lvl+1)
                childSumMap[node]=(node.left.val if node.left else 0)+(node.right.val if node.right else 0)
                
                
        popLevelSums(root)
        
        def solve(node,parent,lvl):
            if not node:
                return
            if parent!=None:
                solve(node.left,node,lvl+1)
                solve(node.right,node,lvl+1)
                node.val = lvlSum[lvl] - childSumMap[parent]
            else:
                solve(node.left,node,lvl+1)
                solve(node.right,node,lvl+1)
                node.val = 0
        solve(root,None,0)
        return root
        