class Solution:
    def reorganizeString(self, s: str) -> str:
        
        hp = []
        ans = ""
        ctr = Counter(s)
        
        for c,cnt in ctr.items():
            heappush(hp,(-cnt,c))
        
        while len(hp)>1:
            mfccnt,mfc,smfccnt,smfc = *heappop(hp),*heappop(hp)
            ans += mfc+smfc
            mfccnt+=1
            smfccnt+=1
            if mfccnt!=0:
                heappush(hp,(mfccnt,mfc))
            if smfccnt!=0:
                heappush(hp,(smfccnt,smfc))
            
        if len(hp)==0:
            return ans
        else:
            if hp[0][0]<-1:return ""
            return ans+hp[0][1]
        