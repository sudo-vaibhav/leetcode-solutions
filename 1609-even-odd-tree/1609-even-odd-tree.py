# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        
        
        q = deque()
        curLevel = 0
        q.append(root)
        while q:
            shouldHaveOdd = curLevel%2==0
            shouldBeIncreasing = shouldHaveOdd
            lenQ = len(q)
            prev = None
            
            # print(curLevel,q)
            for i in range(lenQ):
                cur = q.popleft()
                
                if (int(shouldHaveOdd) ^ int(cur.val%2==1)) == 1:
                    return False
                
                if i==0:
                    pass
                else:
                    if shouldBeIncreasing and prev>=cur.val:
                        return False
                    if (not shouldBeIncreasing) and prev<=cur.val:
                        return False
                prev = cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            curLevel+=1
            
        return True