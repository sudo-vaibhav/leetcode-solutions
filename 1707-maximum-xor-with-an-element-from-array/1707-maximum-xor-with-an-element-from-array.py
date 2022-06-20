class Solution:
    @cache
    def getNum(self,num):
        NUM = bin(num)[2:]
        NUM= ["0" for _ in range(self.TLEN-len(NUM))]+list(NUM)
        return NUM
    def closest(self,trie,num):
        if len(trie.keys())==0:
            return -1
        ans,tmp = 0,trie
        NUM = self.getNum(num)
        for bitIdx in range(self.TLEN):
            bit = 1 if NUM[bitIdx]=="1" else 0
            flippedBit = 1-bit
            if flippedBit in tmp:
                ans |=1
                tmp = tmp[flippedBit]
            else:
                tmp = tmp[bit]
            ans<<=1
        return ans>>1
    
    def insert(self,trie,num):
        num = self.getNum(num)
        tmp = trie
        for bitIdx in range(self.TLEN):
            bit = 1 if num[bitIdx]=="1" else 0
            tmp = tmp[bit]
            
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        self.TLEN = len(bin(max(max(nums),max([q[0] for q in queries]))))-2
        Trie = lambda : defaultdict(Trie)
        nums.sort()
        trie = Trie()
#         query - base,upperBound        
        base,ub,origIdx = range(3)
        queries = [(q[0],q[1],idx) for idx,q in enumerate(queries)]
        queries.sort(key=lambda x:x[ub])
        ans = [None]*len(queries)
        iter = 0
        for Base,UB,OrigIdx in queries:
            while iter<len(nums) and nums[iter]<=UB:
                self.insert(trie,nums[iter])
                iter+=1
            # print(iter,Base,nums)
            temp = self.closest(trie,Base)
            ans[OrigIdx] = temp
        return ans