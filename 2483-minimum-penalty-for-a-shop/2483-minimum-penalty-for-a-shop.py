class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        n = len(customers)
        ctr = Counter(customers)
        Y = ctr["Y"]
        c = 0
        ach = {
            
        }
        
        for i in range(len(customers)):
            N_count = i-c
            Y_count = (Y-c)
            tot =N_count+Y_count
            # print(i,tot,ach)
            if tot not in ach:
                ach[tot]=i
            c+=customers[i]=="Y"
        if n-Y not in ach:
            ach[(n-Y)]=n
        # print(ach.keys())
        temp =min(ach.keys())
        
        # print(temp,ach[temp])
        return ach[temp]
                