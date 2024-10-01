class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        r = defaultdict(int)
        for i in arr:
            m = i%k
            if m!=0:
                r[m]+=1
        # print(r)
        for i in r:
            if k-i==i:
                if r[k-i]%2!=0:
                    return False
            elif r[k-i]!=r[i]:
                return False
        return True
            