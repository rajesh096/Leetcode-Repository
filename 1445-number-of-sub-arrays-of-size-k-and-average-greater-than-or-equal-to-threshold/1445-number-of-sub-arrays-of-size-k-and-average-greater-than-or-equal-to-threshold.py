class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        s=0
        count=0
        for i in range(k):
            s+=arr[i]
        if(s/k >=t):
            count+=1
        for i in range(len(arr)-k):
            s-=arr[i]
            s+=arr[k+i]
            if(s/k >= t):
                count+=1
        return count