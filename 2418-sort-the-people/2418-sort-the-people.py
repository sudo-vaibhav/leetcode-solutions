class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        return map(lambda x:x[1],sorted((-heights[i],names[i]) for i in range(len(names))))