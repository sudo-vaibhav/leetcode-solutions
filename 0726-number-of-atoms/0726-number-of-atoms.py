class Solution:
    def countOfAtoms(self, f: str) -> str:
        
        i = 0
        
        s = []
        f = "("+f+")"
        n = len(f)
        def merge(target,v):
            for i in v:
                target[i]+=v[i]
        def multiply(d,k):
            for i in d:
                d[i]*=k
        def add(d,k,c):
            d[k]+=c
        def parseNum(i):
            if i>=n:
                return 1,i
            if not f[i].isdigit():
                return 1,i
            ans = ""
            while i<n and f[i].isdigit():
                ans += f[i]
                i+=1
            return int(ans),i
        def getElem(i):
            elem = f[i]
            i+=1
            while i<n and f[i].isalpha() and f[i].islower():
                elem += f[i]
                i+=1
            # print(elem,i)
            return elem,i
        while i<n:
            # print(i,f[i])
            if f[i]=="(":
                s.append(defaultdict(int))
                i+=1
            elif f[i]==")":
                i+=1
                temp,i = parseNum(i)
                # print(")",temp,i,s[-1])
                multiply(s[-1],temp)
                if len(s)>1:
                    v = s.pop()
                    merge(s[-1],v)
            else:
                elem,i = getElem(i)
                # print(elem,i)
                temp,i = parseNum(i)
                # print(elem,temp,i)
                add(s[-1],elem,temp)
        # print(len(s))
        # fin = defaultdict(int)
        # for i in s:
        #     for k in i:
        #         fin[k]+=i[k]
        temp = list(s[-1].items())
        temp.sort()
        
        ans = ""
        for i in temp:
            ans += i[0]
            if i[1]>1:
                ans+=str(i[1])            
        return ans
#             if f[i]=="(":
#                 s.append("(")
#             elif f[i]==")":
#                 while s[-1]!="(":
                
#                 s.pop()
#             else:
#                 elem = ""
#                 start = i
#                 while start==i or (i<n and s[i].isalpha() and s[i].upper()!=s[i]):
#                     elem += s[i]
#                     i+=1
                
#                 getCount(i)
#                 while
                
                    
    
    def joinAtoms(self,p,q):
        atoms = set(p.keys()).union(q.keys())
        final = defaultdict(int)
        
        for k in atoms:
            final[k] = p[k]+q[k]
        return final
    
    