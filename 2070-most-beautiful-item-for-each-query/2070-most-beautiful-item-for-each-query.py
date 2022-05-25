# offline query optimisation
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        sortedQ = sorted(queries)
        items.sort()
        queryAns = {}
        iter = 0
        ans = 0
        for q in sortedQ:
            while iter<len(items):
                price,beauty = items[iter]
                if q<price:
                    break
                ans = max(ans,beauty)
                iter+=1
            queryAns[q] = ans
        
        return [queryAns[q] for q in queries]