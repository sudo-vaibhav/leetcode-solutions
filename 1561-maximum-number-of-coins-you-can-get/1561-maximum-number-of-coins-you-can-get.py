class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        # print(piles)
        
        i=0
        j=n-2
        ans = 0
        while i<=j:
            ans+=piles[j]
            j-=2
            i+=1
        return ans