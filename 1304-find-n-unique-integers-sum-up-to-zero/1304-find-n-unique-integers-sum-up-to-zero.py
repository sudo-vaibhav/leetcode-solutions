class Solution:
    def sumZero(self, n: int) -> List[int]:
        f, temp = n//2,[0]*(n%2)
        for i in range(1,f+1):
            temp.extend([i,-i])
        return temp