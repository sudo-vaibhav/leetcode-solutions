"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        
        def solve(i,j,n):
            if n==1:
                return Node(grid[i][j],True,None,None,None,None)
            half = n//2
            res = list(map(lambda x:solve(*x),[(i,j,half),(i,j+half,half),(i+half,j,half),(i+half,j+half,half)]))
            
            if all(map(lambda x:x.val==res[0].val,res)) and res[0].val in [0,1]:
                # self.isLeaf = True
                # self.val = res[0].val
                return Node(res[0].val,True)
            else:
                # self.isLeaf = False
                # self.val = None
                # self.topLeft = res[0]
                # self.topRight = res[1]
                # self.bottomLeft = res[2]
                # self.bottomRight = res[3]
                return Node(None,False,*res)

        
        return solve(0,0,len(grid))