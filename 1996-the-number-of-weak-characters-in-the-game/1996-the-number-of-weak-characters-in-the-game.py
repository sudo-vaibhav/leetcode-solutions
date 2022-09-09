class Solution:
    def numberOfWeakCharacters(self, props: List[List[int]]) -> int:
        props.sort()
        n = len(props)
        attack,defense = range(2)
        l,r = n-1,n-1
        weak = 0
        # while l>=0 and props[l][attack]==props[r][attack]:
        #     l-=1
        maxDefSeen = -inf
        while l>=0:
            L = l
            while l>=0 and props[l][attack]==props[L][attack]:
                while r>=0 and props[r][attack]>props[L][attack]:
                    maxDefSeen = max(maxDefSeen,props[r][defense])
                    r-=1
                if props[l][1]<maxDefSeen:
                    weak+=1
                l-=1
        return weak