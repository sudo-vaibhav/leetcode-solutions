class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        temp = set()
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                ans.append(i)
        return ans