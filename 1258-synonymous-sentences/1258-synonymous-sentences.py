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
        
        for word in wordBank:
            uf.find(word)
        prev = [""]
        for word in sent:
            base = uf.find(word)
            candidates = []
            for w in wordBank:
                if uf.find(w)==base:
                    # print(w,base)
                    candidates.append(w)
            candidates.sort()
            cur = []
            for cand in candidates:
                for temp in prev:
                    if temp=="":
                        cur.append(cand)
                    else:
                        cur.append(temp+" "+cand)
            prev = cur
        return sorted(prev)