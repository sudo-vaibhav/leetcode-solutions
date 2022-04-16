class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCharCnt = 0
        r,l = 0,0
        n = len(s)
        ans = -inf
        presentChars = {}
        
        while r<n:
            cur = s[r]
            if cur in presentChars:
                presentChars[cur]+=1
            else:
                presentChars[cur]=1
            
            if presentChars[cur]>maxCharCnt:
                maxCharCnt = presentChars[cur]
            
            otherChars = r-l+1-maxCharCnt
            while otherChars > k and l<n:
                if presentChars[s[l]]!=cur:
                    otherChars-=1
                    presentChars[s[l]]-=1
                    if presentChars[s[l]]==0:
                        del presentChars[s[l]]
                l+=1
                
            ans = max(ans,r-l+1)
            r+=1
                
            
        return ans