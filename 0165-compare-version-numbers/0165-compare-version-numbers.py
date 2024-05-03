class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        
        def solve(v1,v2):
            if len(v1)>len(v2): return -solve(v2,v1)
            while len(v1)<len(v2): v1.append(0)
            for i in range(len(v1)):
                cur1,cur2 = v1[i],v2[i]
                if cur1<cur2: return -1
                elif cur1>cur2: return 1
            return 0
        
        return solve(*map(lambda x:list(map(int,x)),map(lambda x:x.split("."),[v1,v2])))
        