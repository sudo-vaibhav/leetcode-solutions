class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        n = len(s)
        ans = num
        for i in range(n):
            for j in range(i+1,n):
                l = list(s)
                l[j],l[i]=l[i],l[j]
                newS = "".join(l)
                if int(newS)>ans:
                    ans = int(newS)
        return ans