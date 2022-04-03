class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = defaultdict(int)
        losses = defaultdict(int)
        players = set()
        for m in matches:
            w,l = m
            wins[w]+=1
            losses[l]+=1
            players.add(l)
            players.add(w)
        v1,v2 = [],[]
        for player in players:
            if losses[player]==0:
                v1.append(player)
            elif losses[player]==1:
                v2.append(player)
        
        return [sorted(v1),sorted(v2)]
            