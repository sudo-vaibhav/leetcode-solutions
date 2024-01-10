# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        adj = defaultdict(list)
        
        def lvr(node,prev=None):
            if node:
                if prev:
                    adj[node.val].append(prev)
                if node.left:
                    adj[node.val].append(node.left.val)
                    lvr(node.left,node.val)
                if node.right:
                    adj[node.val].append(node.right.val)
                    lvr(node.right,node.val)
        lvr(root)
        # print(adj)
        q = deque([start])
        t = 0
        seen = set([start])
        while q:
            lenQ = len(q)
            
            for _ in range(lenQ):
                cur = q.popleft()
                for v in adj[cur]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
            
            t+=1
        return t-1
                