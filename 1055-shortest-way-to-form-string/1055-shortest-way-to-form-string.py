class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sc,tc = set(source),set(target)
        
        for c in tc:
            if c not in sc:
                return -1
        
        n = len(target)
        
        # dp = [[inf if i!=j else 1 for j in range(n)] for i in range(n)]
        # for start in range(n):
        #     for end in range(start,n):
        #         dp[]
        firstOcc = {}
        for idx,i in enumerate(source):
            if i not in firstOcc:
                firstOcc[i] = idx
        m = len(source)
        ti = 0
        si = m
        ans = 0
        while ti<n:
            if si==m:
                si = firstOcc[target[ti]]
                ans+=1
            while si<m and source[si]!=target[ti]:
                si+=1
            if si<m:
                ti+=1
                si+=1
            # if si==m:
                
                
            
        return ans