class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = []
        for k,v in c.items():
            if v==2:
                res.append(k)
        xor = 0
        for i in res:
            xor = xor ^ i
        return xor