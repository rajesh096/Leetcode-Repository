class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float("inf")
        i,j=0,0
        count=0
        f=False
        while(j<len(nums)):
            count+=nums[j]
            if count>=target:
                n=j-i+1
                mini=min(mini,n)
                count-=nums[i]
                count-=nums[j]
                i+=1
                f=True
            else:
                j+=1
            # if j==len(nums):
            #     count-=nums[i]
            #     count-=nums[j-1]
            #     i+=1
            #     j-=1
        if f:
            return mini
        else:
            return 0