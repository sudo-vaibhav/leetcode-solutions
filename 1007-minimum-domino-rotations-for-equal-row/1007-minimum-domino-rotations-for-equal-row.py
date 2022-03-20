class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        c = defaultdict(int)
        
        tc = Counter(tops)
        bc = Counter(bottoms)
        
        for i in range(n):
            if tops[i]==bottoms[i]:
                c[tops[i]]+=1
            else:
                c[tops[i]]+=1
                c[bottoms[i]]+=1
        
        for i in range(1,6+1):
            if c[i]==n:
                break
        else:
            return -1
        ans = float("inf")
        for i in range(1,6+1):
            if c[i]==n:
                ans = min(ans,min(c[i]-tc[i],c[i]-bc[i]))
        return ans