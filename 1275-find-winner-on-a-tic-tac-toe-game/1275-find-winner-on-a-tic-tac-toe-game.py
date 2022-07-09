class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        tt = [["" for _ in range(3)] for _ in range(3)]
        
        def checkDraw():
            for i in range(3):
                for j in range(3):
                    if tt[i][j]=="":
                        return False
            return True
                    
        def checkWinner():
            
#             rowwise check
            
            for row in range(3):
                if tt[row]==["A"]*3:
                    return "A"
                elif tt[row]==["B"]*3:
                    return "B"
            
#             colwise check
            for col in range(3):
                curColVals = []
                for row in range(3):
                    curColVals.append(tt[row][col])
                if curColVals == ["A"]*3 or curColVals == ["B"]*3:
                    return curColVals[0]
            
#             upper diag check
            upperD = [tt[i][i] for i in range(3)]
            if upperD == ["A"]*3 or upperD == ["B"]*3:
                return upperD[0]
            
            lowerD = [tt[i][2-i] for i in range(3)]
            if lowerD == ["A"]*3 or lowerD == ["B"]*3:
                return lowerD[0]

            return False
            
        for idx,move in enumerate(moves):
            if idx%2==0:
                cur = "A"
            else:
                cur = "B"
            
            tt[move[0]][move[1]] = cur
            
            temp =  checkWinner()
            if temp!=False:
                return temp
            if checkDraw():
                return "Draw"
        
        return "Pending"
            
            