class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={k:v for k,v in (zip(set(nums),[0 for i in range(len(nums))]))}
        res=[]
        for i in nums:
            dic[i]+=1
        for i,j in dic.items():
            if j>(len(nums)//3):
                res.append(i)
        return res