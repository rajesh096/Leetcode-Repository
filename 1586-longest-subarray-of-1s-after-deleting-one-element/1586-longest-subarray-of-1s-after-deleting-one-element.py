class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if(len(set(nums))==1 and set(nums)!={0}):
            return len(nums)-1
        l1=[0]
        l2=[]
        c=0
        for i in range(1,len(nums)):
            if(nums[i-1]==1):
                c+=1
                l1.append(c)
            else:
                c=0
                l1.append(c)
        x=0
        for i in range(len(nums)-2,-1,-1):
            if(nums[i+1]==1):
                x+=1
                l2.append(x)
            else:
                x=0
                l2.append(x)
        l2=l2[::-1]
        l2.append(0)
        maxi=0
        print(l1)
        print(l2)
        for i in range(len(nums)):
            maxi=max(maxi,(l1[i]+l2[i]))
        return maxi