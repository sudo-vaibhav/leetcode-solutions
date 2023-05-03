class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        n1,n2 = map(set,[nums1,nums2])
        
        return [n1.difference(n2),n2.difference(n1)]