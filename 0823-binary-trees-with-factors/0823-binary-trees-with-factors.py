class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr,n = list(sorted(arr,reverse=False)),len(arr)
        MOD = (10**9)+7
        
        ansDict = {}
        # print(arr)
        
        for i in range(n):
            ans = 1 # only you as root
            for j in range(i):
                if arr[i]%arr[j]==0:
                    num1 = arr[i]//arr[j]
                    num2 = arr[i]//num1
                    if num1 in ansDict and num2 in ansDict:
                        # print(arr[i],num1,num2)
                        ans = (ans+ansDict[num1]*ansDict[num2])%MOD
            ansDict[arr[i]]=ans
        # print(ansDict)
        return sum(ansDict.values())%MOD