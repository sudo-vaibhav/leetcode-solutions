class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(healths)
        arr = list(zip(positions,healths,directions,range(n)))
        
        arr.sort()
        
        st = []
        
#         for p,h,d,i in arr:
#             if not st or st[-1][2]==d:
#                 st.append([p,h,d,i])
#             else:
#                 if st[-1][1]>h:
#                     st[-1][1]-=1
#                 elif st[-1][1]<h:
#                     st.pop()
#                     st.append((p,h-1,d,i))
#                 else:
#                     st.pop()
        
        for p,h,d,i in arr:
            while st and st[-1][2]=="R" and d=="L":
                if st[-1][1]>h:
                    st[-1][1]-=1
                    break
                elif st[-1][1]<h:
                    st.pop()
                    h-=1
                else:
                    st.pop()
                    break
            else:
                st.append([p,h,d,i])
                
        st.sort(key= lambda x:x[-1])
        return map(lambda x:x[1],st)