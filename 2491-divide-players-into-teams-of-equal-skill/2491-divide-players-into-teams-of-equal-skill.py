class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        tc = len(skill)//2
        s = sum(skill)
        if s%tc!=0:
            return -1
        perteam = s//tc
        c = Counter(skill)
        # print(perteam,c)
        ans = 0
        for p in skill:
            if c[p]>0:
                rem = perteam-p
                if c[rem]==0:
                    return -1
                c[rem]-=1
                c[p]-=1
                ans += p*rem
        return ans
        