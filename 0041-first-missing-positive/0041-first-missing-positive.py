class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set(filter(lambda x:x>0,nums)))
        i=1 
        try:
            while True:
                if nums[i-1]!=i:
                    return i
                i+=1
        except:
            return len(nums)+1