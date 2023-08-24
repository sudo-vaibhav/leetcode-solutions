class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        q=deque(words)
        ans = []
        
        while len(q):
            cur_line = []
            
            
            if len(q)==1 or (maxWidth-len(q[0])-1)<len(q[1]):
                ans.append(q[0]+" "*(maxWidth-len(q[0])))
                q.popleft()
            else:
                total_len = len(q[0])
                taken = [q.popleft()]
                while len(q) and len(taken)+len(q[0])+total_len<=maxWidth:
                    taken.append(q.popleft())
                    total_len+=len(taken[-1])
                
                remaining_space = maxWidth-total_len
                temp = ""
                left_spaces = remaining_space
                ideal = ceil(remaining_space/(len(taken)-1))
                if len(q)==0:
                    for idx, w in enumerate(taken):
                        temp+=w
                        if len(taken)-1!=idx:
                            temp+=" "
                # x*r+(r-1)*y=remaining_space
                else:
                    for idx, w in enumerate(taken):
                        temp+=w
                        if len(taken)-1!=idx:
                            spaces_rendered = ideal if (ideal-1)*(len(taken)-1-idx)<left_spaces else ideal-1
                            temp += " "*spaces_rendered
                            left_spaces-=spaces_rendered
                # print(temp,len(temp))
                ans.append(temp+" "*(maxWidth-len(temp)))
        return ans