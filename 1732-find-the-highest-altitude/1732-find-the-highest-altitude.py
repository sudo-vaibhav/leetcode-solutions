class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prev = 0
        ans = 0
        for num in gain:
            prev+=num
            ans = max(ans,prev)
        return ans