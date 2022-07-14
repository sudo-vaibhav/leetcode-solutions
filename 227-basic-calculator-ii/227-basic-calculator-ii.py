class Solution:
    def calculate(self, s: str) -> int:
        
        
        
        # num,sign = 0,"+"
        
        i,num,sign,st = 0,0,"+",[]
        
        def update(num,sign):
            if sign=="+":st.append(num)
            elif sign=="-":st.append(-num)
            elif sign=="*":st.append(st.pop()*num)
            elif sign=="/":st.append(int(st.pop()/num))
                
        while i<len(s):
            cur = s[i]
            if cur.isdigit():
                num = num*10 + int(cur)
            elif cur in "+-/*":
                update(num,sign)
                num,sign = 0,cur
            elif cur == "(":
                num,disp = self.calculate(s[i+1:])
                i = i+disp
            elif cur == ")":
                update(num,sign)
                return sum(st),i+1
            i+=1
        
        update(num,sign)
        return sum(st)