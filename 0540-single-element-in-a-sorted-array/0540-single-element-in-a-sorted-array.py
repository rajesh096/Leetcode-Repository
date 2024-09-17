class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s=0
        e=len(nums)-1
        while(s<=e):
            mid=(s+e)//2
            a=nums[mid-1] if mid!=0 else float("-inf")
            b=nums[mid+1] if mid!=len(nums)-1 else float("inf")
            if(nums[mid]!=b and nums[mid]!=a):
                return nums[mid]
            elif(nums[mid]==a):
                if((mid)%2==0):
                    e=mid-1
                else:
                    s=mid+1
            else:
                if((mid+1)%2==1):
                    s=mid+1
                else:
                    e=mid-1