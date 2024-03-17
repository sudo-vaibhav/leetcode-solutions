class Solution(object):
    def minimizeStringValue(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        n=len(s)
        
        ans = []
        hp = [0]*26
        for i in s:
            if i!="?":
                hp[ord(i)-ord("a")]+=1
#         for i in range(26):
#             heappush(hp,(0,chr(ord("a")+i)))

        for i in range(n):
            if s[i]=="?":
                # f,c=heappop(hp)
                j = hp.index(min(hp))
                ans.append(chr(ord("a")+j))
                hp[j]+=1
                # heappush(hp,(f+1,c))
            # else:
            #     hp[ord(s[i])-ord("a")]+=1
                # ans.append(s[i])
        f = deque(sorted(ans))
        
        res = []
        for i in s:
            if i!="?":
                res.append(i)
            else:
                res.append(f.popleft())
        return "".join(res)