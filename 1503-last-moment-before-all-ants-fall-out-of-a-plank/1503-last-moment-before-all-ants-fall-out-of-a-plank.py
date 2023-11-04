class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left or [0]),n-min(right or [n]))
        # comb = [*[(i,-1) for i in left],*[(i,1) for i in right]]
        # comb.sort()   
        # st = []
        # ans = 0
        # for pos,x in comb:
        #     print(st,ans,(pos,x))
        #     if x==1:
        #         st.append(pos)
        #     else:
        #         if not st:
        #             ans = max(ans,pos)
        #         else:
        #             toRight = st.pop()
        #             dist = (pos-toRight)
        #             toRightNew =  toRight+dist//2 if dist%2==0 else ceil(toRight+dist/2)
        #             toLeftNew = pos-dist//2 if dist%2==0 else floor(pos-dist/2)
        #             ans = max(ans,toLeftNew)
        #             st = [toRightNew]
        # if st:
        #     return max(ans,n-st[0])
        # return ans
        # # return max(ans,n-st[0])