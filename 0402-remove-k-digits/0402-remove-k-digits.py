class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        chunks = num.split("0")
        ans = []
        # print(chu)
        # for chunk in chunks:
        #     if len(chunk)==0:
        #         ans.append("")
        #         continue
        #     if k>=len(chunk):
        #         k-=len(chunk)
        #     else:
        #         temp = ""
        st = []
        for i in range(len(num)):
            # st.append(chunk[i])
            # if and k>0 and chunk[i]
            if st:
                while st and k>0 and num[i]<st[-1]:
                    st.pop()
                    k-=1
            st.append(num[i])
        while k>0:
            st.pop()
            k-=1
        # ans.append()
#                     if k>0:
                        
                        
#                         k-=1
#                     else:
#                         temp += chunk[i]
                # ans.append(chunk)
            # else:
            #     for c in 
        res= "".join(st).lstrip("0")#("0".join(ans)).lstrip("0")
        return res if len(res) else "0"