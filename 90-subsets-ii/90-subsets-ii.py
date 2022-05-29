class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        prev = [[]]
        for i in range(len(nums)):
            tempans = []
            if i>0 and nums[i]==nums[i-1]:
                for subset in prev:
                    tempans.append(subset+[nums[i]])
            else:
                for subset in ans:
                    tempans.append(subset+[nums[i]])
            prev = tempans
            ans.extend(tempans)
        return ans
            