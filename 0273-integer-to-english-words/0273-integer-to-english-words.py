class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        num = str(num)[::-1]
        bChunk = num[9:10]
        mChunk = num[6:9][::-1]
        tChunk = num[3:6][::-1]
        uChunk = num[0:3][::-1]
        chunks = [bChunk,mChunk,tChunk,uChunk]
        # print(chunks)
        wordMap = {
            "1":"One",
            "2":"Two",
            "3":"Three",
            "4":"Four",
            "5":"Five",
            "6":"Six",
            "7":"Seven",
            "8":"Eight",
            "9":"Nine",
            "0":""
        }
        
        tWordMap = {
            # "1":"One",
            "2":"Twenty",
            "3":"Thirty",
            "4":"Forty",
            "5":"Fifty",
            "6":"Sixty",
            "7":"Seventy",
            "8":"Eighty",
            "9":"Ninety",
            # "0":""
        }
        
        combMap = {
            "10":"Ten",
            "11":"Eleven",
            "12":"Twelve",
            "13":"Thirteen",
            "14":"Fourteen",
            "15":"Fifteen",
            "16":"Sixteen",
            "17":"Seventeen",
            "18":"Eighteen",
            "19":"Nineteen"
        }
        def wordForm(chunk):
            chunk = chunk[::-1]
            d1,d2,d3 = chunk[2:3],chunk[1:2],chunk[0:1]
            ans = []
            
            if d1 and d1!="0":
                ans.append(wordMap[d1])
                ans.append("Hundred")
            
            custom = bool(d2 and d2=="1")
            
            if d2 and d2!="0":
                if not custom:
                    ans.append(tWordMap[d2])
                else:
                    combined =  d2+d3
                    ans.append(combMap[combined])
            if d3 and d3!="0" and not custom:
                ans.append(wordMap[d3])
            
            return " ".join(ans)
        res = []
        for idx,chunk in enumerate(chunks):
            temp = wordForm(chunk)
            if temp:
                res.append(temp)
                if idx==0:
                    res.append("Billion")
                elif idx==1:
                    res.append("Million")
                elif idx==2:
                    res.append("Thousand")
        # print(res)
        
        return " ".join(res)