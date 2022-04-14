class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        q = deque()
        steps=0
        q.append("0000")
        if "0000" in deadends: return -1
        visited = set()
        visited.add("0000")
        while q:
            qs = len(q)
            for i in range(qs):
                cur = q.popleft()
                if cur==target: return steps
                
                for i in range(4):
                    f = list(cur)
                    options = map(str,[(int(f[i])+1)%10,(int(f[i])-1)%10])
                    for opt in options:
                        c = list(f)
                        c[i]=opt
                        c = "".join(c)
                        if c not in visited and c not in deadends:
                            visited.add(c)
                            q.append(c)
            steps+=1
        return -1