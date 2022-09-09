class Solution:
    def numberOfWeakCharacters(self, props: List[List[int]]) -> int:
        props.sort()
        n = len(props)
        # print(props)
        l,r = n-1,n-1
        weak = 0
        while l>=0 and props[l][0]==props[r][0]:
            l-=1
        maxDefSeen = -inf
        while l>=0:
            L = l
            while l>=0 and props[l][0]==props[L][0]:
                while r>=0 and props[r][0]>props[L][0]:
                    maxDefSeen = max(maxDefSeen,props[r][1])
                    r-=1
                if props[l][1]<maxDefSeen:
                    weak+=1
                l-=1
                
        # print(l,r)
        return weak