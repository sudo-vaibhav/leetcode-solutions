class Solution(object):
    def combinationSum2(self, candidates, target):
        ctr = Counter(candidates)
        uniques = list(ctr.keys())
        N,ans = len(uniques),[]
        def solve(idx,target,path=[]):
            # if idx==N:
            if target==0:
                ans.append(list(path))
            else:
                if idx>=N:return
                cur = uniques[idx]
                for pickCount in range(0,ctr[cur]+1):
                    if pickCount*cur<=target:
                        solve(idx+1,target-pickCount*cur,path+[cur]*pickCount)
        solve(0,target,[])
        return ans
    
#         candidates.sort()
#         N = len(candidates)
#         ans = []
#         def solve(idx,target,path):
#             # if idx==N:
#             if target==0:
#                 ans.append(list(path))
#             else:
#                 for i in range(idx,N):
#                     if i>idx and candidates[i]==candidates[i-1]:continue
#                     if candidates[i]>target:break
#                     path.append(candidates[i])
#                     solve(i+1,target-candidates[i],path)
#                     path.pop()
                    
                    
#         solve(0,target,[])
#         return ans