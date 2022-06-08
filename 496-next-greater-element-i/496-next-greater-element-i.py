class Solution:
    def nextGreaterElement(self, qry: List[int], nums2: List[int]) -> List[int]:
        
        grtr = defaultdict(lambda : -1)
        st = []
        for num in nums2:
            if len(st)==0 or st[-1]>num:
                st.append(num)
            else:
                while len(st)!=0 and st[-1]<num:
                    grtr[st[-1]] = num
                    st.pop()
                st.append(num)
        
        return [grtr[num] for num in qry]
                