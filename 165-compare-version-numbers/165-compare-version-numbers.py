class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        i,j,m,n = 0,0,len(v1),len(v2)
        
        while i<m or j<n:
            val1,val2 = 0,0
            while i<m and v1[i]!=".":
                val1*=10
                val1+=int(v1[i])
                i+=1
            i+=1
            
            while j<n and v2[j]!=".":
                val2*=10
                val2+=int(v2[j])
                j+=1
            j+=1
            
            if val1<val2:
                return -1
            elif val1>val2:
                return 1
        
        return 0
                