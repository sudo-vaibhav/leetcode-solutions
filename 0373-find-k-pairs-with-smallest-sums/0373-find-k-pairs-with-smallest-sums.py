class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0]+nums2[0],0,0)]
        
        i,j = 0,0
        m,n = map(len,[nums1,nums2])
        def legal(t):
            return t[0]<m and t[1]<n
        ans = []
        seen = set([(0,0)])
        while len(ans)<k and heap:
            s,p1,p2 = heappop(heap)
            
            ans.append((nums1[p1],nums2[p2]))
            
            t1,t2 = (p1+1,p2),(p1,p2+1)
            
            if legal(t1) and t1 not in seen:
                heappush(heap,(nums1[t1[0]]+nums2[t1[1]],*t1))
                seen.add(t1)
            if legal(t2) and t2 not in seen:
                heappush(heap,(nums1[t2[0]]+nums2[t2[1]],*t2))
                seen.add(t2)
        
        return ans
            
            