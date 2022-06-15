# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque()
        q.append((root,1))
        depth =  0
        while q:
            # print(q[-1][1],q[0][1])
            ans = max(ans,q[-1][1]-q[0][1]+1)
            lenQ = len(q)
            begin = q[0][1]
            for i in range(lenQ):
                cur,idx = q.popleft()
                idx-=begin
                if cur.left:
                    q.append((cur.left,idx*2))
                if cur.right:
                    q.append((cur.right,1+(idx*2)))
            depth+=1
        return ans
        
        