class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        def ms(l,r):
            nonlocal ans
            if l<r:
                mid = (l+r)//2
                ms(l,mid)
                ms(mid+1,r)
                i,j = l,mid+1
                temp = [0]*(r-l+1)
                while i<=mid:
                    while j<=r and nums[i]>nums[j]*2:
                        j+=1
                    ans += j-mid-1
                    i+=1
                i,j,k = l,mid+1,0
                while i<=mid and j<=r:
                    if nums[i]<=nums[j]:
                        temp[k] = nums[i]
                        i+=1
                    else:
                        temp[k] = nums[j]
                        j+=1
                    k+=1
                while i<=mid:
                    temp[k] = nums[i]
                    i,k = i+1,k+1
                while j<=r:
                    temp[k] = nums[j]
                    j,k = j+1,k+1
                k = 0
                i = l
                while i<=r:
                    nums[i] = temp[k]
                    i,k = i+1,k+1
        ms(0,len(nums)-1)
        return ans        