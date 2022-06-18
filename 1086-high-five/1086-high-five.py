class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        
        for stud, mark in items:
            heappush(scores[stud],mark)
            if len(scores[stud])>5:
                heappop(scores[stud])
        
        ans = []
        for stud in scores:
            tot = sum(scores[stud])
            # print(tot,scores[stud])
            ans.append((stud,tot//5))
        
        return sorted(ans,key=lambda x:x[0])