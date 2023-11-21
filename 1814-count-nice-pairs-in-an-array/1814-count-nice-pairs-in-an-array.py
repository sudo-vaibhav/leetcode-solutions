class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num:int):
            return int(str(num)[::-1])
        MOD = 10**9+7
        ans = 0
        arr = list(map(lambda x:(x,rev(x)),nums))
        # x + rev(y) = y + rev(x)
        # x - rev(x) = y - rev(y)
        occs = defaultdict(int)
        for j in range(len(nums)):
            temp = nums[j]-rev(nums[j])#arr[j][1]
            ans += occs[temp]
            if ans>=MOD:
                ans-=MOD
            occs[temp]+=1
        return ans