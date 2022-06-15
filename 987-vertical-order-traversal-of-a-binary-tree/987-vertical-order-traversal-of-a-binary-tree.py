# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedDict,SortedList
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        colMap = SortedDict({})
        
        def vlr(node,row=0,col=0):
            if not node: return
            else:
                if not col in colMap:
                    colMap[col]=SortedDict({})
                if row not in colMap[col]:
                    colMap[col][row] = SortedList()
                colMap[col][row].add(node.val)
                vlr(node.left,row+1,col-1)
                vlr(node.right,row+1,col+1)
        vlr(root)
        ans = []
        for col in colMap:
            temp = []
            for row in colMap[col]:
                temp.extend(colMap[col][row])
            ans.append(temp)
        return ans