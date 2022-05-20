class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        i=0
        while i<n:
            I = nums[i]
            j=i+1
            while j<n:
                J = nums[j]
                l = j+1
                r = n-1
                
                pre = nums[i]+nums[j]
                while l<r:
                    L,R = nums[l],nums[r]
                    temp = L+R
                    if temp==target-pre:
                        ans.append([nums[i],nums[j],L,R])
                        while l<n and nums[l]==L:
                            l+=1
                        while r>=0 and nums[r]==R:
                            r-=1
                            
                    elif temp<target-pre:
                        while l<n and nums[l]==L:
                            l+=1
                    else:
                        while r>=0 and nums[r]==R:
                            r-=1
                while j<n and J==nums[j]:
                    j+=1
            while i<n and I==nums[i]:
                i+=1
        return ans
                    