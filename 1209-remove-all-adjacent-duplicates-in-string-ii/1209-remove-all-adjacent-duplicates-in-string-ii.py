class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        q = deque()
        for i in s:
            if len(q)>0 and q[-1][0]==i:
                q.append((i,q[-1][1]+1))
            else:
                q.append((i,1))
            if q[-1][1]==k:
                for _ in range(k):
                    q.pop()
                    
        ans="".join(( i[0] for i in q))
        return ans
            
        