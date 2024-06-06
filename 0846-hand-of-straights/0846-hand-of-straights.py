class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hp = []
        
        c = Counter(hand)
        if len(hand)%groupSize!=0:
            return False
        for i in c:
            heappush(hp,(i,c[i]))
        while hp:
            if len(hp)<groupSize:
                return False
            
            used = [heappop(hp) for _ in range(groupSize)]
            for i in range(1,groupSize):
                if used[i][0]-used[i-1][0]!=1:
                    return False
            newCaps = list(filter(lambda x:x[1]!=0,[(x,y-min(map(lambda x:x[1],used))) for x,y in used]))
            for i,j in newCaps:
                heappush(hp,(i,j))
        return True