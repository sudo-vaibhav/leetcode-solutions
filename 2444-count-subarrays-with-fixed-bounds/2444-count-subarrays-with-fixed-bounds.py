class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        # minh,maxh = [],[]
        
        split = []
        
        chunks = []
        
        for i in nums:
            if i<minK or i>maxK:
                chunks.append(split)
                split = []
            else:
                split.append(i)
        if len(split):
            chunks.append(split)
        # print(chunks)
        # return 0
        def findconst(chunk,ll,rl):
            l,r = -1,-1
            for i in range(len(chunk)):
                if ll==chunk[i]:
                    l = i
                if rl==chunk[i] and r==-1:
                    r = i
            return (l,r)
        ans = 0
        for chunk in chunks:
            # lastOcc = len(chunk)
            nextOccs = []
            mi,ma = len(chunk),len(chunk)
            for i in range(len(chunk)-1,-1,-1):
                if chunk[i]==minK:
                    mi = i
                if chunk[i]==maxK:
                    ma = i
                nextOccs.append((mi,ma))
            for i in range(len(chunk)):
                nmi,nma = nextOccs[i]
                if nmi!=len(chunk) and nma!=len(chunk):
                    ans += len(chunk)-max(nmi,nma)
        return ans
#             l,r = findconst(chunk,maxK,minK)
#             print(chunk,l,r)
#             if l>-1 and r>-1:
#                 ans += (l+1)*(len(chunk)-r)
            
#             print(chunk,l,r)
#             if l>-1 and r>-1:
#                 ans += (l+1)*(len(chunk)-r)
            
        return ans