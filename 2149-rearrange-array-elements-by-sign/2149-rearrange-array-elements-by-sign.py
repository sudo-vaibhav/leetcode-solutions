class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        return [x for row in zip(filter(lambda x:x>=0,nums),filter(lambda x:x<0,nums)) for x in row]