class Solution:
    def findClosest(self,trie,target):
        tmp = trie
        ans = 0
        for bit in target:
            if bit in tmp:
                ans = ans|1
                tmp = tmp[bit]
            else:
                tmp = tmp[1-bit]
            ans<<=1
        return ans>>1
    def insert(self,trie,num):
        tmp = trie
        for bit in num:
            tmp = tmp[bit]
    def findMaximumXOR(self, nums: List[int]) -> int:
#      biggest num binary representation length in array
        n = len(bin(max(nums)))-2
        Trie = lambda : defaultdict(Trie)
        trie = Trie()
#       redefine nums
        nums = [[int((num & (1<<i))!=0) for i in range(n-1,-1,-1)] for num in nums]
        # print(nums)
        ans = 0
        for num in nums:
            flipped = [1-bit for bit in num]
            closest = self.findClosest(trie,flipped) 
            ans = max(ans,closest)
            self.insert(trie,num)
        return ans