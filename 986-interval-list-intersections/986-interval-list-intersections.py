class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        i,j,n,m,ans = 0,0,len(fl),len(sl),[]
        def getOp(iv1,iv2):
            interval = [max(iv1[0],iv2[0]),min(iv1[1],iv2[1])]
            if interval[0]<=interval[1]:return interval
            return False
                
        while i<n and j<m:
            curI,curJ = fl[i],sl[j]
            op = getOp(curI,curJ)
            
            if op!=False:
                opTill = op[1]
                ans.append(op)
                if curI[1]==opTill:
                    i+=1
                if curJ[1]==opTill:
                    j+=1
            else:
                nexI,nexJ = [inf,0],[inf,0]
                if i<n-1:
                    nexI = fl[i+1]
                if j<m-1:
                    nexJ = sl[j+1]
                
                if nexI[0]<nexJ[0]:
                    i+=1
                else:
                    j+=1
        return ans