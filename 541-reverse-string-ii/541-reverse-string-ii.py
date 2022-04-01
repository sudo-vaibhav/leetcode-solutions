class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        temp = []
        i=0
        n = len(s)
        while i<n:
            u=""
            
            upperBound = min(n,i+2*k) 
            while i<upperBound:
                u+=s[i]
                i+=1
                
            
            u = u[:k][::-1]+u[k:]
            temp.append(u)
            
        print(temp)
        
        return "".join(temp)
            