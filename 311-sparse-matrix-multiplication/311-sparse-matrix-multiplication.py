
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
    
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m,k,n = len(mat1),len(mat1[0]),len(mat2[0])
#         row by row vecs
        m1vecs = []
        for i in range(m):
            m1vecs.append(SparseVector(mat1[i]))        
            
    
#     col by col vecs
        m2vecs = []
    
        for j in range(n):
            # print(mat2[:][j])
            temp = []
            for i in range(k):
                temp.append(mat2[i][j])
            m2vecs.append(SparseVector(temp))
        # print(m1vecs,m2vecs)
        ans = [[None for _ in range(n)] for _ in range(m)]      
        for i in range(m):
            for j in range(n):
                ans[i][j] = m1vecs[i].dotProduct(m2vecs[j])
        return ans