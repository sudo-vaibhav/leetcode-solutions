class Solution:
   def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        cog
        + log
          + 
        + dog
        """
        def ppath(p):
            if d.get(p):
                path.append(p)
                if d[p][1]==-1:
                    # print(path[::-1])
                    ans.append([v for v in path[::-1]])
                else:
                    for v in d:
                        if d[v][0]+1==d[p][0] and sum([1 for i in range(k) if v[i]!=p[i]])<=1:
                            ppath(v)
                path.pop(-1)
            pass
            
        n, k = len(wordList), len(wordList[0])
        
        # build tries
        tries = {}
        for i in range(n):
            for j in range(k):
                w = wordList[i][:j] + "?" + wordList[i][j+1:]
                tries[w] = tries.get(w, [])                
                tries[w].append(wordList[i])
            pass
        
        # print(beginWord, endWord)
        # print("[build] tries: ", tries)
        
        # bfs (only closing node after 1-level)
        q = [beginWord]
        d = {q[0]: (0, -1)}
        flag = False
        while len(q)>0:
            u = q.pop(0)
            for j in range(k):
                w = u[:j] + "?" + u[j+1:]
                for v in tries.get(w, []): # for all v adjacent u
                    if not d.get(v):
                        d[v] = (d[u][0]+1, u)
                        q.append(v)
                    if v==endWord:
                        break
                if d.get(endWord):
                    break
            if d.get(endWord):
                    break
                        
#         print("\n[bfs] d: ", d)
        
#         print("\npath: ")
        
        path = []
        ans = []
        ppath(endWord)
        # print("=" * 20)
        return ans