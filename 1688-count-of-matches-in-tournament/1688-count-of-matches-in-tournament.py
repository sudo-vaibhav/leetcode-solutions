class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n<=1:
            return 0
        else:
            if n%2==0:
                return (n//2)+self.numberOfMatches(n//2)
            else:
                return ((n-1)//2)+self.numberOfMatches(1+(n-1)//2)
            