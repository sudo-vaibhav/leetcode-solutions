class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n,pos,steps = len(arr),defaultdict(list),0
        seen,q = set([n-1]),deque([n-1])
        for idx, i in enumerate(arr): pos[i].append(idx)
        while q:
            lenQ = len(q)
            for _ in range(lenQ):
                cur = q.popleft()
                if cur == 0: return steps
                for i in filter(
                    lambda x:0<=x<n and x not in seen,
                    set([cur-1,cur+1,*pos[arr[cur]]])
                ):
                    seen.add(i)
                    q.append(i)
                del pos[arr[cur]]
            steps+=1
                     
                
                
        