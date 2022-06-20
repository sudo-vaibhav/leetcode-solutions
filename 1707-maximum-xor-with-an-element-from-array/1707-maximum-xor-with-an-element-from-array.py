class Solution:
    def closest(self,trie,num):
        if len(trie.keys())==0: return -1
        ans,tmp = 0,trie
        for i in range(self.TLEN-1,-1,-1):
            bit = (num>>i)&1
            flippedBit = 1-bit
            if flippedBit in tmp:
                ans |=1
                tmp = tmp[flippedBit]
            else:
                tmp = tmp[bit]
            ans<<=1
        return ans>>1
    
    def insert(self,trie,num):
        tmp = trie
        for i in range(self.TLEN-1,-1,-1):
            bit = (num>>i)&1
            tmp = tmp[bit]
            
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        self.TLEN = len(bin(max(max(nums),max([q[0] for q in queries]))))-2
        Trie = lambda : defaultdict(Trie)
        nums.sort()
        trie,iter,ans = Trie(),0,[None]*len(queries)
        base,ub,origIdx = range(3)
        queries = sorted([(q[0],q[1],idx) for idx,q in enumerate(queries)],key=lambda x:x[ub])
        for Base,UB,OrigIdx in queries:
            while iter<len(nums) and nums[iter]<=UB:
                self.insert(trie,nums[iter])
                iter+=1
            # print(iter,Base,nums)
            temp = self.closest(trie,Base)
            ans[OrigIdx] = temp
        return ans