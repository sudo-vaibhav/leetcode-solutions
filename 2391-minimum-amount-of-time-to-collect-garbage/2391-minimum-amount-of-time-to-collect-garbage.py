class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        x = list(map(Counter,garbage))
        lastOcc = defaultdict(int)
        types = "MPG"
        for h in types:
            for i in range(len(garbage)):
                if h in garbage[i]:
                    lastOcc[h] = i
        # print(lastOcc)
        ans = 0
        for cur in "MPG":
            temp = 0 if lastOcc[cur]==0 else sum(travel[:lastOcc[cur]])
            # print(x,temp)
            temp += sum(map(lambda v:v[cur],x))
            # print(cur,temp)
            ans += temp
        return ans