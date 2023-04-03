class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        c = 0
        
        people.sort()
        
        i,j = 0,len(people)-1
        
        while i<=j:
            s = people[i]+people[j]
            if s<=limit:
                i+=1
                j-=1
            else:
                j-=1
            c+=1
        
        return c