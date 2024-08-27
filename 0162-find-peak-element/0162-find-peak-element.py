class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        
        s=0
        e=len(nums)-1
        while(s<=e):
            mid=(s+e)//2
            if(mid==len(nums)-1):
                if (nums[mid]>nums[mid-1]):
                    res=mid
                    break
                else:
                    e=mid-1
            elif (mid==0):
                if(nums[mid]>nums[mid+1]):
                    res=mid
                    break
                else:
                    s=mid+1
            else:
                if(nums[mid]>nums[mid+1]):
                    if(nums[mid-1]<nums[mid]):
                        res=mid
                        break
                    else:
                        e=mid-1
                else:
                    s=mid+1
        return res