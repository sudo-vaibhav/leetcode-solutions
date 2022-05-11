class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        cnt = [[0]*26 for i in range(n)]
        a = ord("a")
        ans = 0
        
        def getBeauty(j,i):
            if j==-1:
                prev = [0]*26
            else:
                prev = cnt[j]
            cur = cnt[i]
            maxDiff,minDiff = 0,inf
            for i in range(26):
                temp = cur[i]-prev[i]
                if temp>maxDiff:
                    maxDiff = temp
                if temp<minDiff and temp!=0:
                    minDiff = temp
            if maxDiff!=0 and minDiff!=inf:
                return maxDiff-minDiff
            else:
                return 0
        for i in range(n):
            cur = s[i]
            if i>0:
                cnt[i] = list(cnt[i-1])
            cnt[i][ord(cur)-a]+=1
            for j in range(-1,i):
                temp = getBeauty(j,i) 
                # if temp>0:
                #     print(j,i,temp,cnt[j],cnt[i])
                ans+=temp
        return ans