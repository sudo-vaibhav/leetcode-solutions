class Solution:
    def compress(self, chars: List[str]) -> int:
        k = 0
        l,r = 0,0
        n  = len(chars)
        while r<n:
            
            while r<n and chars[r]==chars[l]:
                r+=1
            
            cnt = r-l
            
            chars[k] = chars[l]
            k+=1
            if cnt>1:
                cnt = str(cnt)
                for c in cnt:
                    chars[k] = c
                    k+=1
            l = r
        
        return k