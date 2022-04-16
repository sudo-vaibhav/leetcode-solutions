class Solution:
    def sumZero(self, n: int) -> List[int]:
        f = n//2
        temp = []
        for i in range(1,f+1):
            temp.append(i)
            temp.append(-i)
        
        if n%2==1:
            temp.append(0)
        return temp