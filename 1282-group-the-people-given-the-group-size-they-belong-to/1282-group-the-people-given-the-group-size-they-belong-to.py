class Solution:
    def groupThePeople(self, gs: List[int]) -> List[List[int]]:
        
        grps = defaultdict(list)
        
        ans = []
        
        for i in range(len(gs)):
            grps[gs[i]].append(i)
            if len(grps[gs[i]])==gs[i]:
                ans.append(list(grps[gs[i]]))
                grps[gs[i]]=[]
        return ans