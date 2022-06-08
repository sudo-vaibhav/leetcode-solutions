# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        ans = root.val
        ansLvl = 1
        
        def lot(node):
            nonlocal ans,ansLvl
            if not node: return
            q = deque()
            q.append(node)
            lvl = 1
            while q:
                n = len(q)
                s = 0
                for _ in range(n):
                    cur = q.popleft()
                    s+=cur.val
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                if s>ans:
                    ansLvl = lvl 
                    ans = s
                lvl+=1
                
        lot(root)
        return ansLvl