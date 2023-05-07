class Solution:
    def longestObstacleCourseAtEachPosition(self, obs: List[int]) -> List[int]:
        
        
        # obs = [(idx,v) for idx, v in enumerate(obstacles)]
        # print(obs)
        # obs.sort(key=lambda x:x[1])
        ans = []
        lis = []
        for v in obs:
            # print(idx,v)
            idx = bisect.bisect_right(lis,v)
            if idx==len(lis):
                lis.append(v)
            else:
                lis[idx]=v
            
            ans.append(idx+1)
        return ans