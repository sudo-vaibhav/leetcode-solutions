# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
#         depths = {}
#         seen = set()
#         nodeMap = {}
#         def populateDepths(node,curDepth=0):
#             if not node:
#                 return
#             depths[node.val]=curDepth
#             nodeMap[node.val]=node
#             populateDepths(node.left,curDepth+1)
#             populateDepths(node.right,curDepth+1)
          
#         populateDepths(root)
#         ans = {}
#         sDepths = SortedList(depths.values())
#         queries = [(depths[q],q,idx) for idx,q in enumerate(queries)]
        
#         def solve(node):
#             if not node or node.val in seen:
#                 return
#             seen.add(node.val)
#             sDepths.remove(depths[node.val])
#             solve(node.left)
#             solve(node.right)
#         levelCache = {}
#         for d,q,i in sorted(queries,reverse=True):
#             solve(nodeMap[q])
#             ans[i] = sDepths[-1]
#         return [ans[i] for i in range(len(queries))]
        lvlOrder = defaultdict(SortedList)
        depths = {}
        contribs = {}
        def populateDepths(node,curDepth=0):
            if not node:
                return 0
            l = populateDepths(node.left,curDepth+1)
            r = populateDepths(node.right,curDepth+1)
            depths[node.val]=curDepth
            contribution = max(l,r,curDepth)
            lvlOrder[curDepth].add(contribution)
            contribs[node.val]=contribution
            return contribution
        populateDepths(root)
        ans = []
        
        for q in queries:
            lvl = depths[q]
            if len(lvlOrder[lvl])==1:
                ans.append(lvl-1)
            else:
                lvlOrder[lvl].remove(contribs[q])
                ans.append(lvlOrder[lvl][-1])
                lvlOrder[lvl].add(contribs[q]) # add it back
        return ans
                
            
            
