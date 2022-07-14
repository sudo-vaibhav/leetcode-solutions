class Solution:
    def fractionToDecimal(self, num: int, den: int) -> str:
        if num==0:return "0"
        neg = False
        if num<0 and den<0:
            num *= -1
            den *= -1
        else:
            if num<0 or den<0:
                neg = True
                num = abs(num)
                den = abs(den)
        
        remainderSeen = {}
        
        preDecimal = num//den
        
        remainder = num - preDecimal*den
        k = 0
        ans = str(preDecimal)
        if remainder == 0:
            ans = str(preDecimal)
        else:
            remSoFar = ""
            repeating = inf
            i=0
            while remainder!=0:
                # if k==7:
                #     break
                # print(remSoFar,remainder)
                remainder*=10
                if remainder in remainderSeen:
                    repeating = remainderSeen[remainder]
                    # ans += "."+"("+remSoFar+")"
                    break
                else:
                    # if remainder not in remainderSeen:
                    remainderSeen[remainder]=i
                    remSoFar+=str(remainder//den)
                    remainder = remainder-(remainder//den)*den
                i+=1
                # k+=1
            # else:
            #     ans += "."+remSoFar
            # print(num,den,repeating,remainderSeen,remSoFar)
            if repeating!=inf:
                # print(repeating,remSoFar)
                ans =  ans + "."+remSoFar[:repeating]+"("+remSoFar[repeating:]+")"
            else:
                ans = ans + "."+remSoFar
        # print(ans,neg)
        return ("-" if neg else "") + str(ans)