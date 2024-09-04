class Solution:
    def nextGreater(self, arr, val):
        if len(arr)==0:
            return inf
        if arr[-1]<=val:
            return inf
        l,r = 0,len(arr)-1
        ans = arr[-1]
        while l<=r:
            m = (l+r)//2
            if arr[m]<=val:
                l = m+1
            else:
                ans = arr[m]
                r = m-1
        return ans
    def nextSmaller(self, arr, val):
        if len(arr)==0:
            return -inf
        if arr[0]>=val:
            return -inf
        l,r = 0,len(arr)-1
        ans = arr[-1]
        while l<=r:
            m = (l+r)//2
            if arr[m]>=val:
                r = m-1
            else:
                ans = arr[m]
                l = m+1
        return ans
    def robotSim(self, commands: List[int], obs: List[List[int]]) -> int:
        lToR = {
            "U" : "R",
            "R": "D",
            "D":"L",
            "L":"U"
        }
        rToL = {
            v:k for k,v in lToR.items()
        }
        xMap = defaultdict(list)
        yMap = defaultdict(list)
        
        for ix,iy in obs:
            xMap[ix].append(iy)
            yMap[iy].append(ix)
        for i in xMap:
            xMap[i] = list(sorted(xMap[i]))
        for j in yMap:
            yMap[j] = list(sorted(yMap[j]))
            
        cur = "U"
        x,y = 0,0
        ans = 0
        for c in commands:
            newX,newY = x,y
            if c<0:
                if c==-2:
                    cur = rToL[cur]
                else:
                    cur = lToR[cur]
            else:
                
                if cur=="U":
                    newY = min(y+c,self.nextGreater(xMap[x],y)-1)
                elif cur=="D":
                    newY = max(y-c,self.nextSmaller(xMap[x],y)+1)
                elif cur=="R":
                    newX = min(x+c,self.nextGreater(yMap[y],x)-1)
                else:
                    newX = max(x-c,self.nextSmaller(yMap[y],x)+1)
            # print(c,ans,x,y,newX,newY,cur)
            x,y = newX,newY
            
            ans = max(ans,x**2+y**2)
        return ans
                