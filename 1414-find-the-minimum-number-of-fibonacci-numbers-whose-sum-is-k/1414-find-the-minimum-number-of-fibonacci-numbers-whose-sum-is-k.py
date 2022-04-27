class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        a,b = 1,1
        fibNos = [1,1]
        
        while fibNos[-1]<k:
            fibNos.append(a+b)
            a,b = b,a+b
        moves,n = 0,len(fibNos)
        for i in range(n-1,-1,-1):
            if fibNos[i]<=k:
                moves+=1
                k-=fibNos[i]
            
        # print(fibNos)
        return moves