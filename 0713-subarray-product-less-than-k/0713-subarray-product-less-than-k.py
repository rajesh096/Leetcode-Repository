class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        s=1
        i,j=0,0
        count=0
        while(j<len(nums)):
            if(nums[j]>=k):
                j+=1
                i=j
                s=1
                continue
            s*=nums[j]
            if(s<k):
                count+=(j-i+1)
                print(count)
                j+=1
            else:
                s=s//nums[i]
                i+=1
                s=s//nums[j]
                # if(s<k):
                #     count+=(j-i+1)
            if i==len(nums):
                break

        return count
            