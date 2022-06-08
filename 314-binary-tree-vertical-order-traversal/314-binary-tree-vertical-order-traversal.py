# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapping = {}
        def dfs(node,offset=0):
            if not node:return
            mapping[node]=offset
            dfs(node.left,offset-1)
            dfs(node.right,offset+1)
        
        ansDict = defaultdict(list)
        
        def lot(node):
            if not node: return
            q = deque()
            q.append(node)
            
            while q:
                cur = q.popleft()
                ansDict[mapping[cur]].append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
                    
        
        
        dfs(root)
        lot(root)
        ansKeys = sorted(ansDict.keys())
        
        ans = []
        for key in ansKeys:
            ans.append(ansDict[key])
        return ans