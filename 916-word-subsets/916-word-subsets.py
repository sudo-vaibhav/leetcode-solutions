class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        mc=[0]*26
        for w in words2:
            temp = Counter(w)
            for k in temp:
                c=ord(k)-ord("a")
                mc[c] = max(mc[c],temp[k])
        ans=[]
        #print(mc)
        def solve(w):
            temp=Counter(w)
            for idx,i in enumerate(mc):
                k = chr(idx+ord("a")) 
                if k not in temp:
                    temp[k]=0
                if temp[k]<i:
                    return False
            return True
        for w in words1:
            if solve(w):
                ans.append(w)
        
        return ans