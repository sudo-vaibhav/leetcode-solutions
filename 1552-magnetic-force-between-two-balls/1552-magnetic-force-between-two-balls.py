class Solution:
    def maxDistance(self, p: List[int], v: int) -> int:
        p.sort()
        l,r = 1,p[-1]-p[0]
        ans = 0
        # print(p)
        def pos(guess):
            last = p[0]
            placed = 1
            for i in p[1:]:
                # a = i-last
                # if guess==500000000:
                #     print(a,guess,last,i)
                if i-last>=guess:
                    last = i
                    placed += 1
            # if guess==500000000:
            #     print(placed,m)
            return placed>=v
        while l<=r:
            m = (l+r)//2
            t = pos(m)
            # print(m,t)
            if t:
                ans = m
                l = m+1
            else:
                r = m-1
        return ans