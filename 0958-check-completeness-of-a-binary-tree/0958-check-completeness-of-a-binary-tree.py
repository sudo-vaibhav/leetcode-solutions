# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        def getHeight(root):
            if not root:
                return 0
            return 1+max(getHeight(root.left),getHeight(root.right))
        
        h = getHeight(root)
        
        curH = 1
        
        q = deque([root])
        prob = False
        while q:
            lenQ = len(q)
            
            for _ in range(lenQ):
                cur = q.popleft()
                if cur.left:
                    if prob: return False
                    q.append(cur.left)
                else:
                    if curH==h:
                        pass
                    elif curH!=h-1:
                        return False
                    else:
                        if not prob:
                            prob = True
                    
                if cur.right:
                    if prob: return False
                    q.append(cur.right)
                else:
                    if curH==h:
                        pass
                    elif curH!=h-1:
                        return False
                    else:
                        if not prob:
                            prob = True
            curH+=1
        
        return True