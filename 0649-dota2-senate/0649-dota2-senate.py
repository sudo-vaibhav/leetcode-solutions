class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        # RRDD
        # RDRD
        
        ansMap = {
            "R":"Radiant",
            "D":"Dire"
        }
        c = Counter(senate)
        if "R" not in c:
            c["R"]=0
        if "D" not in c:
            c["D"]=0
        # if c["R"]==c["D"]:
        #     return ansMap[senate[0]]
        # else :
        #     return ansMap["R"] if c["R"]>c["D"] else ansMap["D"]
        # skip = {"R":0,"D":0}
        banned = {"R":set(),"D":set()}
        pendingBan = {"R":0,"D":0}
        while len(banned["R"])!=c["R"] and len(banned["D"])!=c["D"]:
            for i in range(len(senate)):
                v = senate[i]
                if i not in banned[v]:
                    notV = "R" if v=="D" else "D"
                    if pendingBan[v]:
                        banned[v].add(i)
                        pendingBan[v]-=1
                    else:
                        pendingBan[notV]+=1
                    
        return ansMap["R"] if len(banned["D"])==c["D"] else ansMap["D"]