class Solution:
    def fairCandySwap(self, a: List[int], b: List[int]) -> List[int]:
        
#         def solve(big,small):
#             if sum(big)<sum(small):
#                 return solve(small,big)
            
#             diff = sum(big)-sum(small)
            
#         return solve(aliceSizes,bobSizes)
        smol,big = (a,b) if sum(a)<sum(b) else (b,a)
        bigs = set(big)
        S,B = map(sum,[smol,big])
        bal = (S+B)//2
        for num in smol:
            temp = S-num
            gainReq = bal-temp
            if gainReq in bigs:
                return [num,gainReq] if smol==a else [gainReq,num]
        