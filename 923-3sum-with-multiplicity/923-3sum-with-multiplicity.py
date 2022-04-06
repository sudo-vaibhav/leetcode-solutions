class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count=defaultdict(int)
        mod = int(10**9 + 7)
        for i in arr:
            count[i]+=1
        arr.sort()
        final_answer=0
        @cache
        def fac(n):
            return math.factorial(n)
        for i in range(0,len(arr)-2):
            if(i!=0 and arr[i]==arr[i-1]):
                continue;
            j=i+1
            k=len(arr)-1
            while(j<k):
                if(j!=i+1 and arr[j]==arr[j-1]):
                    j+=1
                elif(k!=len(arr)-1 and arr[k+1]==arr[k]):
                    k-=1
                elif(arr[j]+arr[k]==target-arr[i]):
                    i_count=count[arr[i]]
                    j_count=count[arr[j]]
                    k_count=count[arr[k]]
                    if(arr[i]==arr[k]):
                        final_answer+= fac(i_count)//(fac(i_count-3)*fac(3))
                    elif(arr[i]==arr[j]):
                        final_answer+= k_count*(i_count-1)*(i_count)//2
                    elif(arr[j]==arr[k]):
                        final_answer+= i_count*(j_count-1)*(j_count)//2
                    else:
                        final_answer+=(i_count*j_count*k_count)
                    j+=1
                    k-=1
                elif(arr[j]+arr[k]>target-arr[i]):
                    k-=1
                elif(arr[j]+arr[k]<target-arr[i]):
                    j+=1
                if final_answer>=mod:
                    final_answer-=mod
                
        return final_answer