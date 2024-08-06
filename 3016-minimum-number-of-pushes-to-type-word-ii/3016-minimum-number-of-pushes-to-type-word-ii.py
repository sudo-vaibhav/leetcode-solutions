class Solution:
    def minimumPushes(self, word: str) -> int:
        c = list(Counter(word).items())
        c.sort(key=lambda x:-x[1])
        
        i = 0
        used = defaultdict(int)
        ans = 0
        for ch,num in c:
            used[i]+=1
            ans += used[i]*num
            i = (i+1)%8
        return ans
            
        