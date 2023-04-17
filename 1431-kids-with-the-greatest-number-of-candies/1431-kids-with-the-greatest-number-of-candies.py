class Solution:
    def kidsWithCandies(self, candies: List[int], ec: int) -> List[bool]:
        m = max(candies)
        
        return [i+ec>=m for i in candies]