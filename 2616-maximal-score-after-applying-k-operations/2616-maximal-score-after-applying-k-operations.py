import math
import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res=0
        m=[-n for n in nums]
        heapq.heapify(m)
        for i in range(k):
            maxi=-heapq.heappop(m)
            res+=maxi
            heapq.heappush(m,-(math.ceil(maxi/3)))
        return res