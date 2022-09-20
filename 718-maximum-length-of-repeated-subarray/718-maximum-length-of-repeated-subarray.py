class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        l,r = 1,n
        ans = 0
        def getSets(ws,arr):
            q = deque()
            l,r = 0,0
            seen = set()
            rolling = 0
            base = 102
            mod = 2**63-1
            while r<len(arr):
                if r-l==ws:
                    rolling -= arr[l]*(base**(ws-1))
                    l+=1
                rolling*=base
                rolling+=arr[r]
                r+=1
                if r-l==ws:
                    seen.add(rolling)
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