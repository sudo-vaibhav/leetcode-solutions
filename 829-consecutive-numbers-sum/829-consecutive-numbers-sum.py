class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        
        # N = (x+1)+(x+2)+(x+3)+...+(x+k)
        # N = k*(k+1)/2 + kx
        # 2*N = k(k+1+2x)
        
        # ans = 0
        seen = set()
        for k in range(1,int((2*n)**0.5)+1):
            if (2*n)%k==0:
                
                temp = ((2*n)//k)-k-1
                if temp%2==0:
                    seen.add((k,temp//2))
        
        return len(seen)