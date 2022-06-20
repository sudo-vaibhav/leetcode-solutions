class Solution:
    def findClosest(self,trie,target):
        tmp,ans = trie,0
        for i in range(self.MAXLEN-1,-1,-1):
            bit = 1-(target>>i)&1
            if bit in tmp:
                ans = ans|1
                tmp = tmp[bit]
            else:
                tmp = tmp[not bit]
            ans<<=1
        return ans>>1
    def insert(self,trie,num):
        tmp = trie
        for i in range(self.MAXLEN-1,-1,-1):
            tmp = tmp[(num>>i)&1]
    def findMaximumXOR(self, nums: List[int]) -> int:
        self.MAXLEN = len(bin(max(nums)))-2
        Trie = lambda : defaultdict(Trie)
        trie,ans = Trie(),0
        for num in nums:
            self.insert(trie,num)
            closest = self.findClosest(trie,num) 
            ans = max(ans,closest)
        return ans