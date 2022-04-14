class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outDeg,inDeg = defaultdict(list),defaultdict(list)
        
        for a,b in trust:
            outDeg[a].append(b)
            inDeg[b].append(a)
        # print(outDeg,inDeg)
        for i in range(1,n+1):
            if len(outDeg[i])==0 and len(inDeg[i])>=n-1:
                return i
            
        else:
            return -1