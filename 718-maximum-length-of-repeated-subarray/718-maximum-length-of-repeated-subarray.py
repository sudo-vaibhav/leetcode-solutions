class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        l,r = 1,n
        ans = 0
        def getSets(ws,arr):
            q = deque()
            i = 0
            seen = set()
            while i<len(arr):
                if len(q)==ws:
                    q.popleft()
                q.append(arr[i])
                i+=1
                if len(q)==ws:
                    seen.add(tuple(q))
            return seen
        while l<=r:
            ws = l+(r-l)//2
            
            s1 = getSets(ws,nums1)
            
            for elem in getSets(ws,nums2):
                if elem in s1:
                    ans = ws
                    l = ws+1
                    break
            else:
                r = ws-1
        return ans