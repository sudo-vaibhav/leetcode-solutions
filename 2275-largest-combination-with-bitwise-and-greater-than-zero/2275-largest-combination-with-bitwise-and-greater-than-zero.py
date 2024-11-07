class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bm = defaultdict(int)
        
        for i in candidates:
            bi = 0
            while i>0:
                bm[bi]+=i&1
                i>>=1
                bi+=1
        # print(bm)
        return max(bm.values())
                
                