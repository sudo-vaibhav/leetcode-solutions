class Solution:
    def generateSentences(self, syns: List[List[str]], text: str) -> List[str]:
        sent = text.split()
        
        wordBank = set(sent)
        
        class UF:
            def __init__(self):
                self.parent = {}
                # self.distinct = n
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                if pu==pv:
                    return False
                # self.distinct-=1
                self.parent[pu]=pv
                return True
            def find(self,v):
                if v not in self.parent:
                    self.parent[v]=v
                if self.parent[v]!=v:
                    self.parent[v]=self.find(self.parent[v])
                return self.parent[v]
            def united(self):
                return self.distinct==1
            
        uf = UF()
        for w1,w2 in syns:
            wordBank.add(w1)
            wordBank.add(w2)
            uf.union(w1,w2)
        
        # for word in wordBank:
        #     uf.find(word)
        ans = []
        def solve(idx,path=[]):
            if idx==len(sent):
                ans.append(" ".join(path))
            else:
                base = uf.find(sent[idx])
                candidates = []
                for w in wordBank:
                    if uf.find(w)==base:
                        # print(w,base)
                        candidates.append(w)
                candidates.sort()
                for w in candidates:
                    solve(idx+1,path+[w])
        solve(0)
        
        return ans