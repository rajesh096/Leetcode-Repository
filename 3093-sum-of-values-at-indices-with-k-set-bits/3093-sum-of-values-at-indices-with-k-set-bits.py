class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            x=0
            a=i
            while(a>0):
                if(a&1==1):
                    x+=1
                a>>=1
            print(x)
            if(x==k):
                c+=nums[i]
        return c