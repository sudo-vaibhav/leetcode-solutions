class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        @cache
        def rev(num:int):
            return int(str(num)[::-1])
        MOD = 10**9+7
        ans = 0
        occs = defaultdict(int)
        for num in nums:
            temp = num-rev(num)#arr[j][1]
            ans += occs[temp]
            if ans>=MOD:
                ans-=MOD
            occs[temp]+=1
        return ans