# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth==1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        else:
            
            q = deque()
            
            q.append(root)
            curDep = 1
            while q:
                lenQ = len(q)
                
                for _ in range(lenQ):
                    cur = q.popleft()
                    if curDep==depth-1:
                        leftNode = TreeNode(val,cur.left)
                        rightNode = TreeNode(val,None,cur.right)
                        
                        cur.left = leftNode
                        cur.right = rightNode
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                            
                curDep+=1
                        
            return root