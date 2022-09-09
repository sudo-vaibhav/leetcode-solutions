class Solution:
    def numberOfWeakCharacters(self, props: List[List[int]]) -> int:
        # n = len(props)
        # props.sort()
        # attack,defense = range(2)
        # l,r = n-1,n-1
        # ans,maxDefSeen = 0,-inf
        # while l>=0:
        #     L = l
        #     while l>=0 and props[l][attack]==props[L][attack]:
        #         while r>=0 and props[r][attack]>props[L][attack]:
        #             maxDefSeen = max(maxDefSeen,props[r][defense])
        #             r-=1
        #         if props[l][defense]<maxDefSeen:ans+=1
        #         l-=1
        # return ans
        
        maxDefense = defaultdict(int)
        
        for prop in props:
            maxDefense[prop[0]] = max(maxDefense[prop[0]],prop[1])
        
        for attack in range(100_000,0,-1):
            maxDefense[attack] = max(maxDefense[attack],maxDefense[attack+1])
        # print(maxDefense)  
        weak = 0
        for prop in props:
            if maxDefense[prop[0]+1]>prop[1]:
                weak+=1
        return weak