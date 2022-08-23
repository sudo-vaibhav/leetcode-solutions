class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        candleBefore = [-1]*n
        candleAfter = [n]*n
        
        prev = -1
        for i in range(n):
            if s[i]=="|":
                prev = i
            candleBefore[i] = prev
        
        nex = n
        for i in range(n-1,-1,-1):
            if s[i]=="|":
                nex = i
            candleAfter[i] = nex
        
        # print(candleBefore,candleAfter)
        ans = []
        prefixSum = [0]
        
        for i in s:
            prefixSum.append(prefixSum[-1]+(i=="*"))
            
        for u,v in queries:
            U,V = candleAfter[u],candleBefore[v]
            # print(u,v,U,V)
            plates = prefixSum[V+1]-prefixSum[U]
            ans.append(max(0,plates))
        return ans