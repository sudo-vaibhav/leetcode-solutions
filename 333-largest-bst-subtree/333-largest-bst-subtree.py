# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node: return (0,True,inf,-inf)
            l = dfs(node.left)
            r = dfs(node.right)
            
            isCurBST = True
            if node.left:
                if l[3]>=node.val or not l[1]:
                    isCurBST = False
            if node.right:
                if r[2]<=node.val or not r[1]:
                    isCurBST = False
            
            # ans = max(ans,l[0],r[0],1)
            if isCurBST:
                temp = l[0]+r[0]+1
                ans = max(ans,temp)
            #     return (temp,True,)
            return (l[0]+r[0]+1,isCurBST,min(l[2],r[2],node.val),max(l[3],r[3],node.val))    
                
        dfs(root)
        return ans