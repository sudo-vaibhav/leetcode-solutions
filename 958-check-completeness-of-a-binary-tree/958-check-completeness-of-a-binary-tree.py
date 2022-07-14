# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        def getHeight(node):
            if not node:
                return 0
            return 1+max(getHeight(node.left),getHeight(node.right))
        
        h = getHeight(root)
        
        q = deque()
        level = 1
        q.append(root)
        if h==1:
            return True
        
        while q:
            lenQ = len(q)
            
            if level<=h-1:
                if lenQ!=2**(level-1):
                    return False
            isSecondLastLevel = level==h-1
            isLastLevel = level == h
            childAllowed = True
            for _ in range(lenQ):
                cur = q.popleft()
                if cur.right and not cur.left:
                    return False
                
                if cur.left or cur.right:
                    if not childAllowed:
                        return False
                if not cur.left or not cur.right:
                    if (not isLastLevel and not isSecondLastLevel):
                        return False
                    else:
                        if isSecondLastLevel:
                            childAllowed = False
                    
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            level += 1
        return True        
                
                