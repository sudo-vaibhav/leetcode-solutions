class Solution:
    def accountsMerge(self, acns: List[List[str]]) -> List[List[str]]:
        
        
        class UF:
            def __init__(self):
                self.parent = {}
                
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                if pu==pv:
                    return False
                self.parent[pu]=pv
                return True
            def find(self,v):
                if v not in self.parent:
                    self.parent[v]=v
                
                if self.parent[v]!=v:
                    self.parent[v]=self.find(self.parent[v])
                return self.parent[v]
            
        uf = UF()
        for acct in acns:
            person,*mails = acct
            for mail in mails[1:]:
                uf.union(mails[0],mail)
        
        
        uniquePersons = {}
        mails = defaultdict(set)
        
        for person,*emails in acns:
            temp = uf.find(emails[0])
            uniquePersons[temp]=person
            for m in emails:
                mails[temp].add(m)
        
        ans = []
        
        for pMail in uniquePersons:
            person = uniquePersons[pMail]
            ans.append((person,*sorted(mails[pMail])))
            
        # for person,*mails in acns:
        #     mails[uf.]
        return ans