class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        @cache
        def bCount(idx):
            if idx<0: return 0
            
            return int(s[idx]=="b")+bCount(idx-1)
        
        @cache
        def solve(idx):
            if idx<0: return 0
            
            if s[idx]=="a":
#             now we can either remove current element or keep current element and remove all previous B's
                return min(solve(idx-1)+1,bCount(idx))
            else:
#               no problem in keeping B in tail
                return solve(idx-1)
                
            
        return solve(len(s)-1)