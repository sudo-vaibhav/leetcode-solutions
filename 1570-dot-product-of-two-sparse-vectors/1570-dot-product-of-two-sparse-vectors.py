class SparseVector:
    def __init__(self, nums: List[int]):
        self.mapping = {}
        for idx in range(len(nums)):
            self.mapping[idx] = nums[idx]
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        if len(self.mapping)<len(vec.mapping):
            lessKeys = self.mapping
            other = vec.mapping
        else:
            lessKeys = vec.mapping
            other = self.mapping
        for idx in lessKeys:
            if idx in other:
                ans += lessKeys[idx]*other[idx]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)