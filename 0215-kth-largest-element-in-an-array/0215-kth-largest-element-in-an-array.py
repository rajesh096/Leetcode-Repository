import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=[-num for num in nums]
        res=0
        heapq.heapify(n)
        for i in range(k):
            maxi=heapq.heappop(n)
            res=maxi
        return -res