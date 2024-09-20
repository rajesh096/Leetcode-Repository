class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        num=nums[::-1]
        a=[]
        for i in range((len(num)//2)):
            a.append(num[(len(num)//2)+i])
            a.append(num[i])
            # if(len(nums)//2)+i !=len(nums):
            
        if(len(num)%2==1):
            a.append(num[-1])
        print(a)
        # nums =nums.clear()
        # nums=[]
        for i in range(len(a)):
            nums[i]=a[i]


        