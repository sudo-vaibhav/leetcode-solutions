class Solution:
    def kthPalindrome(self, queries: List[int], il: int) -> List[int]:
        pp = il//2 if il%2==0 else (il+1)//2
        maxPos = 9*(10**(pp-1))
        # print(maxPos)

        def solve(q):
            s=""
            t=maxPos
            if q>maxPos:return -1
            else:
                q-=1
                while len(s)<pp:
                    d = 9 if s=="" else 10
                    t = t//d
                    # if t==0:
                        # s+="0"
                    # else:
                    s+=str(q//t+(1 if s=="" else 0))
                    q = q%t

                rightPart = (s[:-1] if il%2==1 else s)[::-1]
                return int(s+rightPart)

        return [solve(q) for q in queries] 
                            
                
                        
                            
                
                        