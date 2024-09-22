class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def findNumsBetween(n1,n2):
            steps = 0
            while n1<=n:
                steps += min(n+1,n2)-n1
                n1*=10
                n2*=10
            return steps
        cur = 1
        k-=1
        while k:
            temp = findNumsBetween(cur,cur+1)
            if temp<=k:
                cur = cur+1
                k -= temp
            else:
                cur *= 10
                k-=1
        return cur