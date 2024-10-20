class Solution:
    def parseBoolExpr(self, e: str) -> bool:
        n = len(e)
        @cache
        def solve(s):
            print(s)
            if len(s)==1:
                return s=="t"
            else:
                # match s[0]:
                if s[0] == '!':
                    return not solve(s[2:-1])
                ags = []
                brackets = 0
                cur = ""
                for i in s[2:-1]:
                    if i==",":
                        if brackets==0:
                            ags.append(cur)
                            cur = ""
                            continue
                    if i=="(":
                        brackets+=1
                    elif i==")":
                        brackets-=1
                    cur += i
                ags.append(cur)

                if s[0]== '&':
                    # individuals = s[2:-1].split(",")
                    return all(map(solve,ags))
                else:
                #'|':
                    # individuals = s[2:-1].split(",")
                    return any(map(solve,ags))
                    # case '(':
                    #     return solve(s[1:-1])
                        
        return solve(e)