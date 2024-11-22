class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        c = defaultdict(int)
        for row in matrix:
            joined = "".join(map(str,row))
            
            a = joined[0]
            b = "1" if a=="0" else "0"
            pattern = joined.replace(a,"T").replace(b,"F")
            # print(joined,a,b,pattern)
            c[pattern]+=1
        return max(c.values())