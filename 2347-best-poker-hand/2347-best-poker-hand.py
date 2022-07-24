class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if suits == [suits[0]]*5:
            return "Flush"
        ctr = Counter(ranks)
        # print(ctr)
        for v in ctr.values():
            if v>=3:
                return "Three of a Kind"
        for v in ctr.values():
            if v>=2:
                return "Pair"
    
        return "High Card"
        
