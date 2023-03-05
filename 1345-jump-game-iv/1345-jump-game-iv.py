class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        seen = set()
        valSeen = set()
        seen.add(n-1)
        # valSeen.add(arr[n-1])
        q = deque()
        q.append(n-1)
        pos = defaultdict(list)
        for idx, i in enumerate(arr):
            pos[i].append(idx)
            
        steps = 0
        while q:
            
            lenQ = len(q)
            
            for _ in range(lenQ):
                
                cur = q.popleft()
                val = arr[cur]
                if cur==0:
                    return steps
                
                for i in filter(
                    lambda x:0<=x<n,
                    [cur-1,cur+1,*([] if val in valSeen else pos[val])]
                ):
                    
                    if i not in seen:
                        seen.add(i)
                        q.append(i)
                valSeen.add(val)
            steps+=1
                     
                
                
        