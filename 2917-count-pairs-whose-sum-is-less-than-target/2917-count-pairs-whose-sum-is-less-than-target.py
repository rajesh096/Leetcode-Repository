class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count=0
        i,j=0,1
        while i<len(nums):
            if(nums[i]+nums[j]<target and i<j):
                count+=1
                print(nums[i]+nums[j])
            j+=1
            if(j>len(nums)-1):
                i+=1
                j=i+1
                if(i==len(nums)-1):
                    break
        return count