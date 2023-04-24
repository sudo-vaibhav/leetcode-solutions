class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = list([-x for x in stones])
        heapify(hp)
        
        while len(hp)>1:
            s1,s2 = heappop(hp),heappop(hp)
            if s1!=s2:
                heappush(hp,s1-s2)

        return 0 if len(hp)==0 else -hp[0]
        
        