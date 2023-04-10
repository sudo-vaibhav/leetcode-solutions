class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        
        idxs = defaultdict(list)
        
        
        for i,num in enumerate(nums):
            idxs[num].append(i)
            
        ans = [0]*len(nums)
        # print(idxs)
        
        for val in idxs:
            if len(idxs[val])>1:
                running = 0
                s = sum(idxs[val])
                for i,idx in enumerate(idxs[val]):
                    followCount = len(idxs[val])-1-i
                    ans[idx] = abs(running-i*idx)+abs(s-running-idx-followCount*idx)
                    running+=idx
        return ans