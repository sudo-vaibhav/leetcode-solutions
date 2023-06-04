class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        sizes = {}
        children = defaultdict(list)
        root = None
        for idx,par in enumerate(parents):
            if par!=-1:
                children[par].append(idx)
            else:
                root = idx
        
        def getSubtreeSizes(node):
            ans = 1
            # if not node: 
            #     pass
            # else:
            for child in children[node]:
                ans += getSubtreeSizes(child)
            sizes[node]=ans
            return ans
                
        getSubtreeSizes(root)
        ans = 0
        scores = defaultdict(int)
        # print(sizes)
        for node in range(0,len(parents)):
            c1= sizes[children[node][0]] if len(children[node])>0 else 1
            c2  = sizes[children[node][1]] if len(children[node])>1 else 1 
            temp = max(1,sizes[root]-sizes[node])*(c1)*(c2)
            ans = max(ans,temp)
            scores[temp]+=1
        # print(scores)
        return scores[ans]