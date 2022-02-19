import re
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = list(map(int,re.findall("\d+",s)))
        print(nums)
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                return False
        return True