class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = defaultdict(int)
        for domain in cpdomains:
            num,d = domain.split()
            num = int(num)
            dString = ""
            for idx,cur in enumerate(d.split(".")[::-1]):
                if idx==0:
                    dString = cur
                else:
                    dString = cur+"."+dString
                cnt[dString]+=num
        
        ans = []
        for k in cnt:
            ans.append(str(cnt[k])+" "+k)
        return ans