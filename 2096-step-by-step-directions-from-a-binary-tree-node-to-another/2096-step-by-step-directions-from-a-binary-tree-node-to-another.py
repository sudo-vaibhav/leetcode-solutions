# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        adj = defaultdict(list)
        
        
        def constructAdj(node,prev,direction):
            if node:
                if prev!=-1:
                    adj[prev].append((node.val,direction))
                    adj[node.val].append((prev,"U"))
                constructAdj(node.left,node.val,"L")
                constructAdj(node.right,node.val,"R")
                
        
        constructAdj(root,-1,"x")
        seen = set()
        ans = None
        def findWay(node,cur=[]):
            nonlocal ans
            if node==destValue:
                if ans==None or len(cur)<len(ans):
                    ans = "".join(cur)
                # return
            for v,d in adj[node]:
                if v not in seen:
                    seen.add(v)
                    cur.append(d)
                    findWay(v,cur)
                    cur.pop()
                    seen.remove(v)
            
                    
        findWay(startValue)
        return ans