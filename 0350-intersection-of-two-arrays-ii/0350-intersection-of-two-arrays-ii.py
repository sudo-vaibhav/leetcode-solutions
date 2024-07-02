class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = Counter(nums1)
        b = Counter(nums2)
        ans = []
        for k in a:
            ans.extend([k]*min(a[k],b[k]))
        return ans