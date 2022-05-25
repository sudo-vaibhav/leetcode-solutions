# class Solution:
#     def minSessions(self, tasks: List[int], sessionTime: int) -> int:
#         N = len(tasks)
#         perms = set(tuple(permutations(tasks)))  
        
#         ans = inf
#         for perm in perms:
#             tempans = 0
#             cap = 0
#             for task in perm:
#                 if cap<task:
#                     tempans+=1
#                     cap = sessionTime
#                 cap-=task
#             ans = min(ans,tempans)
            
#         return ans

# recursive approach
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        N = len(tasks)
        
        @cache
        def solve(idx,sessions):
            if idx>=N:
                # print(sessions)
                return 0
            else:
                sessions = list(sessions)
                cur = tasks[idx]
                sessions.append(cur)
                ans = 1+solve(idx+1,tuple(sessions))
                sessions.pop()
                
#                 fit in older sessions cases
                for i in range(len(sessions)):
                    if sessions[i]+cur<=sessionTime:
                        sessions[i] += cur
                        ans = min(ans, solve(idx+1,tuple(sessions)))
                        sessions[i] -= cur
                return ans
            
        return solve(0,tuple())









