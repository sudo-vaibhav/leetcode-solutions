class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bmasks = defaultdict(int)
        
        def getBM(word):
            a = ord("a")
            ans = 0
            for i in word:
                ans|=(1<<(ord(i)-a))
            return ans
        
        for word in words:
            bm = getBM(word)
            bmasks[bm] = max(bmasks[bm],len(word))
        # print(bmasks)
        bms = list(bmasks.keys())
        ans = 0
        
        for i in range(len(bms)):    
            bm1 = bms[i]
            for j in range(i+1,len(bms)):
                bm2 = bms[j]
                if bm1&bm2==0:
                    ans = max(ans,bmasks[bm1]*bmasks[bm2])
        
        return ans
        