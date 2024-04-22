class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        
        seen = set()
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        ans = 0
        
        q = deque([["0","0","0","0"]])
        
        while q:
            lenQ = len(q)
            
            for _ in range(lenQ):
                
                cur = q.popleft()
                if "".join(cur)==target:
                    return ans
                for i in range(4):
                    prev = int(cur[i])
                    nex = (prev+1)%10
                    pre = (prev-1)%10
                    
                    cur[i] = str(nex)
                    if "".join(cur) not in deadends and tuple(cur) not in seen:
                        seen.add(tuple(cur))
                        q.append(list(cur))
                        
                    
                    cur[i] = str(pre)
                    if "".join(cur) not in deadends and tuple(cur) not in seen:
                        seen.add(tuple(cur))
                        q.append(list(cur))
                    
                    cur[i] = str(prev)
                    
                    
            ans += 1
        
        return -1