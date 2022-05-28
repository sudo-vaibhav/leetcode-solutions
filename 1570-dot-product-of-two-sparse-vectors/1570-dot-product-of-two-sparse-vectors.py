class SparseVector:
    def __init__(self, nums: List[int]):
        self.mapping = {}
        for idx in range(len(nums)):
            self.mapping[idx] = nums[idx]
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for idx in self.mapping:
            if idx in vec.mapping:
                ans += self.mapping[idx]*vec.mapping[idx]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)