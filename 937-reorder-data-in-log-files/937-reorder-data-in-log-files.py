class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let,dig = [],[]
        
        for log in logs:
            type,*rest = log.split()
            # type = log[:3]
            rest = " ".join(rest)
            
            for c in rest:
                if c.isdigit():
                    dig.append((type,rest))
                    break
            else:                
                let.append((type,rest))    
        
        let.sort(key=lambda x:(x[1],x[0]))
        
        return [l[0]+" "+l[1] for l in let]+[i[0]+" "+i[1] for i in dig]