class Solution:
    def minDeletions(self, s: str) -> int:
        ctr = Counter(s)
        ans = 0
        while True:
            for c in range(ord("a"),ord("a")+26):
                c = chr(c)
                for d in range(ord("a"),ord("a")+26):
                    d = chr(d)
                    if c!=d and ctr[c]>0 and ctr[c]==ctr[d]:
                        ctr[c]-=1
                        ans +=1
                        break
                else:
                    continue
                break
            else:
                return ans

        return ans