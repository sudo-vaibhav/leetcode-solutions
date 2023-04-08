class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [nums2.index(i) for i in nums1]