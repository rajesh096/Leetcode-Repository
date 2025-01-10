class Solution:
    def combinationSum(self, candidates: List[int], t: int) -> List[List[int]]:
        def comsum(temp, ind):
            if(sum(temp) >= t):
                if(sum(temp) == t):
                    result.append(temp[:])
                return
            for i in range(ind, len(candidates)):
                temp.append(candidates[i])
                comsum(temp, i)
                temp.pop()
        
        result = []
        comsum([], 0)
        return result