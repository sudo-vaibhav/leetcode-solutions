class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        pskillmask = defaultdict(int)
        skillmap = defaultdict(int)
        
        for idx,skill in enumerate(req_skills):
            skillmap[skill]=idx
        
        for idx,p in enumerate(people):
            for s in p:
                pskillmask[idx] |= 1<<skillmap[s]
        
        
        # print(pskillmask)
        def sbc(mask):
            c = 0
            while mask:
                mask &= mask-1
                c+=1
            return c
        @cache
        def solve(skillsmask):
            if skillsmask==0: return 0
            ans = (1<<len(people))-1
            for pidx in range(len(people)):
                new_skillmask = skillsmask & ~pskillmask[pidx]
                if new_skillmask!=skillsmask:
                    pmask = 1<<pidx|solve(new_skillmask)
                    if sbc(pmask)<sbc(ans):
                        ans = pmask
            return ans
            
        pmask = solve((1<<len(req_skills))-1)
        # print(pmask)
        ans = []
        for i in range(len(people)):
            if 1<<i& pmask:
                ans.append(i)
        return ans
            
            