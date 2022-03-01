class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        temp = m+n-2 # 8
        m-=1
        n-=1
        bigger = max(m,n)
        numerator = reduce(lambda x,y:x*y,[i for i in range(temp,bigger,-1)],1)
        
        return int(numerator /  reduce(lambda x,y:x*y,[i for i in range(1,min(m,n)+1,1)],1))
        