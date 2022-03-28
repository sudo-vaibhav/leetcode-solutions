class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        try:
            return bool(nums.index(target)+1)
        except:
            return False