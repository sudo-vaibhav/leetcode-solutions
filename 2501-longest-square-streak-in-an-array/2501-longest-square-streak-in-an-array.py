class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = defaultdict(int)
        nums.sort()
        
        for i in nums:
            s[i] = s[i**0.5]+1
        temp = max([s[i] for i in nums])
        return temp if temp!=1 else -1