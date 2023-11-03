class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n,m = len(workers),len(bikes)
        assignedBike = set()
        assignedPeople = set()
        
        dists = []
        
        for i in range(n):
            wx,wy = workers[i]
            for j in range(m):
                bx,by = bikes[j]
                dist = abs(wx-bx)+abs(wy-by)
                
                dists.append((dist,i,j))
        dists.sort()
        ans = [-1]*n
        for entry in dists:
            dist,worker,bike = entry
            if worker not in assignedPeople and bike not in assignedBike:
                ans[worker]=bike
                assignedPeople.add(worker)
                assignedBike.add(bike)
        return ans