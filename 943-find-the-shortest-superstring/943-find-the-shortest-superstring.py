class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        allTaken = (1<<n)-1
        
        @cache
        def kmp(s1,s2):
            w = s2+"#"+s1
            n = len(w)
            lps = [0]*n
            i,l = 1,0
            while i<n:
                if w[i]==w[l]:
                    l+=1
                    lps[i]=l
                    i+=1
                else:
                    if l>0:
                        l = lps[l-1]
                    else:
                        lps[i]=0
                        i+=1
            # print(s1,s2,lps)
            temp = [lps[j] for j in range(len(s2)+1,len(w))]
            if len(temp)==0:
                return 0
#             else:
#                 return max(temp)
            return temp[-1]

        @cache
        def solve(prev,used):
            if used==allTaken:
                return ""
            ans = inf
            ansString = None
            for i in range(n):
                if not (used & (1<<i)):
                    commonLen = kmp(prev,words[i])
                    tempans =words[i][commonLen:]+solve(words[i],used|1<<i)
                    if len(tempans)<ans:
                        ans = len(tempans)
                        ansString = tempans
            return ansString
                    
        return solve("",0)