class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        st = deque()
        
        for ast in asteroids:
            if ast > 0 or len(st)==0:
                st.append(ast)
            else:
                # if st[-1]==-ast:
                #     st.pop()
                # else:
                while st and st[-1]>0 and -st[-1]>=ast:
                    removed = st.pop()
                    if removed==-ast:break
                else: 
                    if (not st or st[-1]<0):
                        st.append(ast)
        
        return st