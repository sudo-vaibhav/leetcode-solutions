class Solution:
    def minChanges(self, s: str) -> int:
        
        
        l,r = 0,len(s)
        ans = 0
        chunks = []
        for i in range(0,len(s),2):
            chunk = s[i:i+2]
            if Counter(chunk)["1"]%2==1:
                ans+=1
            # chunks.append()
        return ans
#         while l<=r:
#             m = (l+r)//2
            
#         return ans