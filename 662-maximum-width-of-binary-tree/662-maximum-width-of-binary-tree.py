# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans,q = 0,deque()
        q.append((root,1))
        while q:
            ans = max(ans,q[-1][1]-q[0][1]+1)
            lenQ,begin = len(q),q[0][1]
            for i in range(lenQ):
                cur,idx = q.popleft()
                idx-=begin
                if cur.left:
                    q.append((cur.left,idx*2))
                if cur.right:
                    q.append((cur.right,1+(idx*2)))
        return ans
        
        