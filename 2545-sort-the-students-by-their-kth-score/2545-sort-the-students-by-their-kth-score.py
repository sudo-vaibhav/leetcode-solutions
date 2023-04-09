class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
        score.sort(key=lambda r:r[k],reverse=True)
        return score