class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        ans = 1
        for i in rolls:
            seen.add(i)
            if len(seen)==k:
                ans +=1
                seen = set()
        
        return ans
        