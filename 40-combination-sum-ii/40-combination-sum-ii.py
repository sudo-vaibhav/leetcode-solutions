class Solution(object):
    def combinationSum2(self, candidates, target):
        ctr = Counter(candidates)
        uniques = list(ctr.keys())
        N,ans = len(uniques),[]
        
        def solve(idx,target,path=[]):
            if idx==N:
                if target==0:
                    ans.append(list(path))
            else:
                cur = uniques[idx]
                for pickCount in range(0,ctr[cur]+1):
                    if pickCount*cur<=target:
                        solve(idx+1,target-pickCount*cur,path+[cur]*pickCount)
        solve(0,target,[])
        return ans
    
        # iterative subsets
        
        # [1,2,3,4]
#         generate all subsets
#         res = {[]}
#         res = {[],[1]}
#         res = {[],[1],[3],[1,3]}

