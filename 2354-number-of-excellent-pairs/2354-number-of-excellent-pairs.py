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
        
        # seen = set()
        ans = 0
        for first in d:
            # rest = k-first
            for num in d[first]:
                # d[first].remove(num)
                for second in d:
                    if first+second>=k:
                        ans += len(d[second])
                
                # d[first].add(num)
        
        return ans
            # d[first]
            # print(num,t)
        