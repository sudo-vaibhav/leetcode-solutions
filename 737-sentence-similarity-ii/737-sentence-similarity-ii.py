class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        class UF:
            def __init__(self):
                self.parent = {}
                self.distinct = inf
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                if pu==pv:
                    return False
                self.distinct-=1
                self.parent[pu]=pv
                return True
            def find(self,v):
                if v not in self.parent:
                    self.parent[v] = v
                if self.parent[v]!=v:
                    self.parent[v]=self.find(self.parent[v])
                return self.parent[v]
            def united(self):
                return self.distinct==1
        
        if len(sentence1)!=len(sentence2):return False
        
        uf = UF()
        for w1,w2 in similarPairs:
            uf.union(w1,w2)
        for i in range(len(sentence1)):
            if uf.find(sentence1[i])!=uf.find(sentence2[i]):
                return False
        
        return True
        