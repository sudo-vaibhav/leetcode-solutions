class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = defaultdict(list)
        seen[0].append(-1)
        r = 0
        ans = 0
        for idx, i in enumerate(nums):
            r += i
            cur = r%k
            ans += len(seen[cur])
            seen[cur].append(idx)
        return ans
            