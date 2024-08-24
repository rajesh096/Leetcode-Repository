class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi=0
        ar=[]
        for i in range(k):
            maxi+=nums[i]
        ar.append(maxi/k)
        for i in range(len(nums)-k):
            maxi-=nums[i]
            maxi+=nums[k+i]
            ar.append(maxi/k)
        a=max(ar)
        print(a)
        return a