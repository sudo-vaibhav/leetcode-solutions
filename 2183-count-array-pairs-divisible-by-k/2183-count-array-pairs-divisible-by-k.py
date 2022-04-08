class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ct = defaultdict(int)
        ans=0
        for a in nums:
            x = gcd(a,k)
            for f in ct:
                if (f*x)%k==0:
                    ans+= ct[f]
            ct[x]+=1
        
        return ans