class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i,j = 0,0
        m,n = len(nums1),len(nums2)
        ans = []
        heap = []
        for i in range(min(k,m)):
            heappush(heap,(nums1[i]+nums2[0],i,0))
        
        while heap and k>0:
            k-=1
            _,i,j = heappop(heap)
            
            ans.append([nums1[i],nums2[j]])
            
            if j+1<n:
                heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
                
        return ans
            