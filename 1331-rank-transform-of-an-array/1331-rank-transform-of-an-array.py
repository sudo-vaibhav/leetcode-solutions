class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(arr)
        ranks = {}
        curRank = 1
        for i, num in enumerate(sortedArr):
            if num not in ranks:
                ranks[num] = curRank
                curRank+=1
        
        return map(lambda x:ranks[x],arr)