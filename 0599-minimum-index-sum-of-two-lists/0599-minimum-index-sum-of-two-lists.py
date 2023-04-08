class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        c1, c2 = {},{}
        for idx,s in enumerate(list1):
            c1[s]=idx
        for idx,s in enumerate(list2):
            c2[s]=idx
        ans = inf
        for s in list1:
            if s in c2:
                ans = min(ans,c2[s]+c1[s])
                
        fin = []
        for s in list1:
            if s in c2 and c2[s]+c1[s]==ans:
                fin.append(s)
        return fin