class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
#         trust,nottrust = defaultdict(int),defaultdict(lambda :n-1)
        
#         for u,v in trust:
#             trust[u]
        
        potentialjudges = set(range(1,n+1))
        trusted =defaultdict(int)
        
        for u,v in trust:
            if u in potentialjudges:
                potentialjudges.remove(u)
            trusted[v]+=1
            
        # print(potentialjudges,trusted)
        for i in potentialjudges:
            if trusted[i]==n-1:
                return i
        return -1