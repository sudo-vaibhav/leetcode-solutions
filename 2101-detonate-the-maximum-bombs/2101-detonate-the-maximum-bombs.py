class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bombs = tuple(map(tuple,bombs))
        ans = 0
        
        @cache
        def getDist(b1,b2):
            return math.sqrt((b1[0]-b2[0])**2+(b1[1]-b2[1])**2)
        for idx,detonator in enumerate(bombs):
            q = deque([idx])
            seen = set(q)
            blown = 0
            
            while q:
                # print (q)
                cur = bombs[q.popleft()]
                blown+=1
                for idx2,target in enumerate(bombs):
                    dist = getDist(cur,target)
                    if dist<=cur[-1] and idx2 not in seen:
                        q.append(idx2)
                        seen.add(idx2)
            ans = max(ans,blown)
        
        return ans