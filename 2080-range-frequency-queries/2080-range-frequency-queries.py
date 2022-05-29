class RangeFreqQuery:

    def combinedMap(self,map1,map2):
        allKeys = set(map1.keys()).union(set(map2.keys()))
        ans = defaultdict(int)
        for key in allKeys:
            ans[key] = map1[key]+map2[key]
        return ans
        
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.arr = arr
        self.t = [defaultdict(int) for i in range(4*self.n)]
        
        
        def build(index,l,r):
            if l==r:
                self.t[index][self.arr[l]]+=1
            else:
                mid = l+(r-l)//2
                build(2*index,l,mid)
                build(2*index+1,mid+1,r)
                self.t[index] = self.combinedMap(self.t[index*2],self.t[1+index*2])
                
            
        build(1,0,self.n-1)
        
    def query(self, left: int, right: int, value: int) -> int:
        
        def stQuery(index,l,r,lq,rq):
            if lq>r or rq<l:return 0
            if lq<=l<=r<=rq:return self.t[index][value]
            mid = l+(r-l)//2
            return stQuery(2*index,l,mid,lq,rq)+stQuery(2*index+1,mid+1,r,lq,rq)
        
        return stQuery(1,0,self.n-1,left,right)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)