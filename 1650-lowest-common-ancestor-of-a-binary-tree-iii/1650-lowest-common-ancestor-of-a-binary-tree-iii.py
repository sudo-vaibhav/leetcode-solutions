"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Q = deque()
        # vis = set()
        # Q.append(p)
        # vis.add(p.val)
        # dist = 0
        # while Q:
        #     lenQ = len(Q)
        #     for _ in range(lenQ):
        #         cur = Q.popleft()
        #         # print(cur)
        #         if cur==q:
        #             return dist
        #         if cur.parent and cur.parent.val not in vis:
        #             vis.add(cur.parent.val)
        #             Q.append(cur.parent)
        #         if cur.left and cur.left.val not in vis:
        #             vis.add(cur.left.val)
        #             Q.append(cur.left)
        #         if cur.right and cur.right.val not in vis:
        #             vis.add(cur.right.val)
        #             Q.append(cur.right)
        #     dist+=1
        temp = p
        visP = set()
        while temp:
            visP.add(temp.val)
            temp = temp.parent
        temp = q
        while temp:
            if temp.val in visP:
                return temp
            temp = temp.parent
        
        
        