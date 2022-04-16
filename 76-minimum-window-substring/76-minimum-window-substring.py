class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # cts = Counter(s)
        ref = {}
        for i in t:
            ref[i] = 1 if i not in ref else ref[i]+1
        
        # print(ref)
        l,r = 1,len(s)
        
        ans = ""
        
        def getPos(k):
            # print("guess",k)
            ct = {}
            i=0
            while i<len(s):
                # print(ct)
                cur = s[i]
                if cur in ct:
                    ct[cur]+=1
                else:
                    ct[cur]=1
                if i>=k:
                    ct[s[i-k]]-=1
                    if ct[s[i-k]]==0:
                        del ct[s[i-k]]
                for c in ref:
                    if c not in ct or ref[c]>ct[c]:
                        break
                else:
                    return s[i-k+1:i+1]
                i+=1
            return False
            
        while l<=r:
            guess = l+(r-l)//2
            
            temp = getPos(guess)
            
            if temp==False:
                l = guess+1
            else:
                ans = temp
                r = guess-1
            
        return ans
        