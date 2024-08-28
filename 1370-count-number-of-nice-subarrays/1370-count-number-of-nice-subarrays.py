class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # i,j=0,0
        # count=0
        # res=0
        # while(i<len(nums)):
        #     if(nums[j]%2==1):
        #         count+=1
        #     if(count==k):
        #         res+=1
        #         j+=1
        #     else:
        #         j+=1
        #     if(j==len(nums)):
        #         count=0
        #         i+=1
        #         j=i
        # return res
        dic=defaultdict(int)
        dic[0]=1
        od=0
        res=0
        for i in nums:
            if i%2==1:
                od+=1
            res+=dic[od-k]
            dic[od]+=1
        return res