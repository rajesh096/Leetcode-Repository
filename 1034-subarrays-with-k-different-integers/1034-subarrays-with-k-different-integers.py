class Solution:
    def fun(self,arr,k):
        i=0
        d={}
        res=0
        for j in range(len(arr)):
            if arr[j] in d:
                d[arr[j]]+=1
            else:
                d[arr[j]] = 1
            while(len(d)>k):
                d[arr[i]]-=1
                if(d[arr[i]]==0):
                    del d[arr[i]]
                
                i+=1
            if(len(d)<=k):
                res+=(j-i+1)
        return res
    def subarraysWithKDistinct(self, arr: List[int], k: int) -> int:
            # return 
            a = self.fun(arr,k)-self.fun(arr,k-1)
            return a