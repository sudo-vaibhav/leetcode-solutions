class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        
        for t in tokens:
            # print(st)
            if t in "+/-*":
                
                b = st.pop()
                a = st.pop()
                match t:
                    case "+":
                        st.append(a+b)
                    case "-":
                        st.append(a-b)
                    case "*":
                        st.append(a*b)
                    case _:
                        st.append(a//b if a*b>=0 else ceil(a/b))
            else:
                st.append(int(t))
        return st[-1]