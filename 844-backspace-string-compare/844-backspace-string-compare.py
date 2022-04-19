class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def goBack(string,i)->int:
            if i<0 or string[i]!="#": return i
            bsCount = 1
            while bsCount>0:
                i-=1
                bsCount-=1
                if i>=0 and string[i]=="#":
                    bsCount+=1
                i-=1
                if i>=0 and string[i]=="#":
                    bsCount+=1
            # print("exiting",i)
            return i
        
                
            
        
        i1,i2 = len(s)-1,len(t)-1
        
        while i1>=0 and i2>=0:
            i1 = goBack(s,i1)
            i2 = goBack(t,i2)
            # print(i1,i2)
            if i1<0 or i2<0:break
            if s[i1]!=t[i2]: return False
            i1-=1
            i2-=1
        # print("final checks")
        i1=goBack(s,i1)
        i2=goBack(t,i2)
        # print("check",i1,i2)
        return i1<0 and i2<0