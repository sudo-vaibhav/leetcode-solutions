# # binary search solution
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         ref = {}
#         for i in t: ref[i] = 1 if i not in ref else ref[i]+1
#         l,r = 1,len(s)
#         ans = ""
#         def getPos(k):
#             ct = {}
#             i=0
#             while i<len(s):
#                 cur = s[i]
#                 if cur in ct:
#                     ct[cur]+=1
#                 else:
#                     ct[cur]=1
#                 if i>=k:
#                     ct[s[i-k]]-=1
#                     if ct[s[i-k]]==0:
#                         del ct[s[i-k]]
#                 for c in ref:
#                     if c not in ct or ref[c]>ct[c]:
#                         break
#                 else:
#                     return s[i-k+1:i+1]
#                 i+=1
#             return False
#         while l<=r:
#             guess = l+(r-l)//2
#             temp = getPos(guess)
#             if temp==False:
#                 l = guess+1
#             else:
#                 ans = temp
#                 r = guess-1    
#         return ans
        
        
# optimised sliding window
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ref = {}
        for i in t: ref[i] = 1 if i not in ref else ref[i]+1
        
        i,n = 0,len(s)
        ct = {}
        ans = s
        l = 0
        pos = False
        
        def isPos(ct,ref):
            for c in ref:
                if c not in ct or ct[c]<ref[c]:
                    return False
            return True
        
        while i<n:
            cur = s[i]
            if cur in ct:
                ct[cur]+=1
            else:
                ct[cur]=1 
            while l<i and (s[l] not in ref or (s[l] in ref and ct[s[l]]>ref[s[l]])):
                ct[s[l]]-=1
                if ct[s[l]]==0:
                    del ct[s[l]]
                l+=1
                
            temp = isPos(ct,ref)
            if temp!=False:
                pos = True
                if i-l+1<len(ans):
                    ans = s[l:i+1]
            i+=1
            
        return ans if pos else ""
            
            
            
        
        