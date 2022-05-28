# class SparseVector:
#     def __init__(self, nums: List[int]):
#         self.mapping = {}
#         for idx in range(len(nums)):
#             self.mapping[idx] = nums[idx]
        

#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec: 'SparseVector') -> int:
#         ans = 0
#         if len(self.mapping)<len(vec.mapping):
#             lessKeys = self.mapping
#             other = vec.mapping
#         else:
#             lessKeys = vec.mapping
#             other = self.mapping
#         for idx in lessKeys:
#             if idx in other:
#                 ans += lessKeys[idx]*other[idx]
#         return ans

class SparseVector:
    def __init__(self, nums: List[int]):
        self.arr = []
        for idx in range(len(nums)):
            if nums[idx]!=0:
                self.arr.append((idx,nums[idx]))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        i,j = 0,0
        while i<len(self.arr) and j<len(vec.arr):
            if self.arr[i][0]==vec.arr[j][0]:
                ans+=self.arr[i][1]*vec.arr[j][1]
                i,j = i+1,j+1
            elif self.arr[i][0]<vec.arr[j][0]:
                i+=1
            else:
                j+=1
        return ans