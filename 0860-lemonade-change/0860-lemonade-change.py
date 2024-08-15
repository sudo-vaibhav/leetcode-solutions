class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        need = {
            5: [{
                
            }],
            10: [{
                5:1
            }],
            20: [{
                5:1,
                10:1
            },{
                5:3
            }]
        }
        cur = defaultdict(int)
        for b in bills:
            done=False
            cur[b]+=1
            needed = need[b]
            for config in needed:
                canDo=True
                for k,v in config.items():
                    if v>cur[k]:
                        canDo=False
                        break
                if canDo:
                    for k,v in config.items():
                        cur[k]-=v
                    done=True
                    break
            if not done:
                return False
        return True
            