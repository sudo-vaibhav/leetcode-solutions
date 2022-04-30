class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ct = defaultdict(int)
        ans = 0
        for t in time:
            left = (60-(t%60))%60
            ans += ct[left]
            ct[t%60]+=1
        return ans
            
        
        # for t in time:
            