class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        steps = 0
        for idx in range(len(plants)):
            cur = plants[idx]
            
            if cur<=cap:
                cap-=cur
                steps+=1
            else:
                cap = capacity-cur
                steps+=2*(idx)+1
                
        return steps