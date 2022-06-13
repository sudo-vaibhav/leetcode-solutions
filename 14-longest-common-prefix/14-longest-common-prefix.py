class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = len(strs)
        idx = 0
        while True:
            char = None
            for i in range(N):
                if len(strs[i])<=idx:
                    return strs[i][:idx]
                else:
                    if char==None:
                        char = strs[i][idx]
                    else:
                        if char!=strs[i][idx]:return strs[i][:idx]
            idx+=1
