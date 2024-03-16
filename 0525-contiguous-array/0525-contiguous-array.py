class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = 0
        r= 0
        c = defaultdict(int)
        c[0]=-1
        for i in range(n):
            r+=1 if nums[i]==1 else -1
            if r not in c:
                c[r]=i
            else:
                ans = max(ans,i-c[r])
        return ans
        # temp = []
        # r = 0
        # for idx,i in enumerate(nums):
        #     if i==1:
        #         r+=1
        #     else:
        #         r-=1
        #     temp.append(r)
        #     if r==0:
        #         ans = max(ans,idx+1)
        # print(temp)
        # return ans
        
#         for i in range(n):
        
        l,r = 1,n
        
        while l<=r:
            m = (l+r)//2

            def isPos():
                oc,zc = 0,0
                L,R = 0,0
                while R<n or L<n:
                    print(L,R,zc,oc)
                    # if oc<m or zc<m:
                    #     if nums[R]==0:
                    #         zc += 1
                    #     else:
                    #         oc += 1
                    #     R+=1
                    # elif oc>m or zc>m:
                    #     if nums[L]==0:
                    #         zc -= 1
                    #     else:
                    #         oc -= 1
                    #     L+=1
                    # else:
                    #     if zc==m and oc==m:
                    #         return True
                    #     else:
                    #         if nums[R]==0:
                    #             zc += 1
                    #         else:
                    #             oc += 1
                    #         R+=1
                    if zc<m and R<n:
                        if nums[R]==0:
                            zc += 1
                        else:
                            oc += 1
                        R+=1
                    else:
                        if nums[L]==0:
                            zc -= 1
                        else:
                            oc -= 1
                        L+=1
                    if zc==m and oc==m:
                        return True
                
#                     else:
#                         if zc==m and oc==m:
#                             return True
#                         else:
#                             if nums[R]==0:
#                                 zc += 1
#                             else:
#                                 oc += 1
#                             R+=1
                            
                return False
            
            if isPos():
                ans = max(ans,m*2)
                l = m+1
            else:
                r = m-1

        return ans
                        
                    