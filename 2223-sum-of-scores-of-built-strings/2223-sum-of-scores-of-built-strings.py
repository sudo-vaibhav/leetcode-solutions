class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        def getZarr(s, z):
            l = 0
            r = 0
            for i in range(1,n):
#                 kick start step
                if i<=r:
                    z[i] = min(z[i-l],r-i+1)
                
# advance ment step
                while i+z[i]<n and s[z[i]]==s[i+z[i]]:
                    z[i]+=1
            
                if i+z[i]-1>r:
                    l = i
                    r = i+z[i]-1
            
# limit recallibration step

        z = [0]*n
        getZarr(s,z)
        # print(z)
        return n+sum(z)
 