class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            temp = 0
            
            while i>0:
                i&=i-1
                temp+=1
            ans.append(temp)
        return ans