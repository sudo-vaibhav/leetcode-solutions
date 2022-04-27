class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ct = Counter(words)
        keys = list(ct.keys())
        arr = [(ct[i],i) for i in keys]
        def func(v1,v2):
            
            if v1[0]!=v2[0]:
                return v2[0]-v1[0]
            else:
                if v1[1]>v2[1]:
                    return 1
                return -1
        
        arr = sorted(arr,key = cmp_to_key(func))
        # print(arr)
        return [g[1] for g in arr[:k]]