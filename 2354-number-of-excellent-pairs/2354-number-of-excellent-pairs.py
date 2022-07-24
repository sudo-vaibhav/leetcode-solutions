class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(set)
        for num in nums:
            orig = num
            t = 0
            while num>0:
                num &= num-1
                t+=1
            d[t].add(orig)
        ans = 0
        for first in d:
            # for num in d[first]:
            for second in d:
                if first+second>=k:
                    ans += len(d[second])*len(d[first])
        return ans
        