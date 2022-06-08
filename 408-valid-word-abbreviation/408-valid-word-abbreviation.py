class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i,j = 0,0
        m,n = len(word),len(abbr)
        
        while i<m and j<n:
            num = ""
            J = j
            while J<n and abbr[J].isdigit():
                if J==j and abbr[J]=="0":return False
                num+=abbr[J]
                J+=1
            if J==j:
#                 not digit
                if word[i]!=abbr[j]:
                    return False
                j+=1
                i+=1
            else:
                temp = int(num)
                j = J
                i+=temp
                
        
        return i==m and j==n