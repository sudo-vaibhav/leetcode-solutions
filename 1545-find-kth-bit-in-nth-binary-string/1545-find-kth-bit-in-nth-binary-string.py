class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        
        def solve(i):
            if i==1:
                return "0"
            temp = solve(i-1)
            return temp+"1"+("".join(map(lambda x:"1" if x=="0" else "0",temp)))[::-1]
        
        return solve(n)[k-1]