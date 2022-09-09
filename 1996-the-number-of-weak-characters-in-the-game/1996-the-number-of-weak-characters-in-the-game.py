class Solution:
    def numberOfWeakCharacters(self, props: List[List[int]]) -> int:
        n = len(props)
        props.sort()
        attack,defense = range(2)
        l,r = n-1,n-1
        ans,maxDefSeen = 0,-inf
        while l>=0:
            L = l
            while l>=0 and props[l][attack]==props[L][attack]:
                while r>=0 and props[r][attack]>props[L][attack]:
                    maxDefSeen = max(maxDefSeen,props[r][defense])
                    r-=1
                if props[l][defense]<maxDefSeen:ans+=1
                l-=1
        return ans