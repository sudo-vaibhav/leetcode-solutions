class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = len(strs)
        idx = 0
        while True:
            char = None
            for s in strs:
                if len(s)<=idx:
                    return s[:idx]
                else:
                    if char==None:
                        char = s[idx]
                    else:
                        if char!=s[idx]:return s[:idx]
            idx+=1
        # return strs[0][:idx]