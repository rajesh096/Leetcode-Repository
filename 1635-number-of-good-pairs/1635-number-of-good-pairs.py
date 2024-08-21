class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=[0 for i in range(len(nums))]
        dic = {k:v for k,v in (zip(nums,a))}
        for i in range(len(nums)):
            dic[nums[i]]+=1
        count=0
        for i,j in dic.items():
            c=j
            count+=((c*(c-1))//2)
        print(dic)
        return count