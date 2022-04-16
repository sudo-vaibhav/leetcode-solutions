class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt = [0,0]
        l,r = 0,0
        ans = 0
        n = len(nums)
        while r<n:
            cur = nums[r]
            cnt[cur]+=1
            while l<n and cnt[0]>k:
                cnt[nums[l]]-=1
                l+=1
            # print(l,r,cnt)
            ans = max(ans,sum(cnt))
            r+=1
        return ans
            