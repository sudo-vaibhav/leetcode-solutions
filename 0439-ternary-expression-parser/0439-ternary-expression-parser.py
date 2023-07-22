class Solution:
    def parseTernary(self, exp: str) -> str:
        
        # args = re.split(r"[?:]",expression)
        # print(args)
        # while len(args)>1:
        #     Fval,Tval,Eval = args.pop(),args.pop(),args.pop()
        #     if Eval=="T":
        #         args.append(Tval)
        #     else:
        #         args.append(Fval)
        # for arg 
#         st = deque()
#         i = 0
#         qns = expression.count("?")
#         while i< len(expression):
            
#             if expression[i] == "?":
#                 pass
#             elif expression[i]==":":
#                 Fval = expression[i+1]
#                 Tval, Eval = st.pop(),st.pop()
#                 if Eval=="T":
#                     st.append(Tval)
#                 else:
#                     st.append(Fval)
#                 i+=1
#             else:
#                 st.append(expression[i])
#             i+=1
        
#         # print(st)
#         return st[0]
        i=0
        def solve():
            nonlocal i
            Eval = exp[i]
            # print(Eval)
            
            if Eval.isdigit() or i==len(exp)-1 or exp[i+1]==":":
                i+=1
                return Eval
            else:
                i+=2
            # i+=2
            Tval = solve()
            i+=1
            Fval = solve()
            ans = Tval if Eval=="T" else Fval
            # print("ans:",ans)
            return ans
        return solve()
                