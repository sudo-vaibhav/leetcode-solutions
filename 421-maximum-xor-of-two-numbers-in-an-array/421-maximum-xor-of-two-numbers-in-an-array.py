class Solution:
    def findClosest(self,trie,target):
        tmp,ans = trie,0
        for i in range(self.MAXLEN-1,-1,-1):
            flippedBit = 1-(target>>i)&1
            if flippedBit in tmp:
                ans,tmp = ans|1, tmp[flippedBit]
            else:
                tmp = tmp[1-flippedBit]
            ans<<=1
        return ans>>1
    def insert(self,trie,num):
        tmp = trie
        for i in range(self.MAXLEN-1,-1,-1):
            tmp = tmp[(num>>i)&1]
    def findMaximumXOR(self, nums: List[int]) -> int:
        Trie = lambda : defaultdict(Trie)
        trie,ans,self.MAXLEN = Trie(),0,len(bin(max(nums)))-2
        for num in nums:
            self.insert(trie,num)
            closest = self.findClosest(trie,num) 
            ans = max(ans,closest)
        return ans