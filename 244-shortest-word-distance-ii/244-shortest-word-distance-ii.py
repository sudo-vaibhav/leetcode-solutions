class WordDistance:

    def __init__(self, W: List[str]):
        self.mapping = defaultdict(list)
        for i, w in enumerate(W):
            self.mapping[w].append(i)
        
    
    @cache
    def shortest(self, word1: str, word2: str) -> int:
        def findClosest(v,arr):
            if v<arr[0]:
                return arr[0]-v
            elif v>arr[-1]:
                return v-arr[-1]
            else:
                i = bisect_left(arr,v)
                return min(abs(arr[i]-v),abs(arr[i-1]-v))
            
        ans = inf
        for option in self.mapping[word1]:
            ans = min(ans,findClosest(option,self.mapping[word2]))
        return ans
