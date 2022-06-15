class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key= lambda x:len(x))
        n = len(words)
        # @cache
        def isPred(i,j):
            w1,w2 = words[i],words[j]
            buf = True
            if len(w2)-len(w1)!=1:return False
            i,j = 0,0
            while i<len(w1) and j<len(w2):
                if w1[i]==w2[j]:
                    i+=1
                    j+=1
                else:
                    if not buf:
                        return False
                    else:
                        j+=1
                        buf = False
            return (i==len(w1) and buf and j==len(w2)-1) or (i==len(w1) and j==len(w2))
        
        @cache
        def solve(i):
            if i==n-1:
                return 1
            else:
                ans = 1
                for j in range(i+1,n):
                    if isPred(i,j):
                        temp = solve(j)
                        if 1+temp>ans:
                            ans = 1+temp
                return ans
        fin = 1
        for start in range(n):
            fin = max(fin,solve(start))
        return fin