class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        usages = defaultdict(list)
        
        for i in range(len(keyName)):
            h,m = map(int,keyTime[i].split(":"))
            
            usages[keyName[i]].append(h*60+m)
            
        ans = set()
        for k in usages:
            usages[k].sort()
            for i in range(2,len(usages[k])):
                if usages[k][i]-usages[k][i-2]<=60:
                    ans.add(k)
                    break
        
        return sorted(list(ans))
            