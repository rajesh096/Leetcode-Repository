import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res=0
        heapq.heapify(nums)
        for i in range(len(nums)):
            m1=heapq.heappop(nums)
            if(m1>=k):
                return res
            m2=heapq.heappop(nums)
            heapq.heappush(nums,(m1*2)+m2)
            res+=1
        return res
