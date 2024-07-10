class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = []
        
        for l in logs:
            if l=="./":
                pass
            elif l=="../":
                if s:
                    s.pop()
            else:
                s.append(l)
        return len(s)