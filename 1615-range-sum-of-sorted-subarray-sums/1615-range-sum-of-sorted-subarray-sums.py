class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub=[]
        for i in range(n):
            for j in range(i+1,n+1):
                sub.append(sum(nums[i:j]))
        sub.sort()
        return (sum(sub[left-1:right]))%1000000007