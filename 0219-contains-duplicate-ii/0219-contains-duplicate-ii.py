class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {k:v for k,v in (zip(set(nums),[[] for i in range(len(nums))]))}
        res=[]
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        for i,j in dic.items():
            if len(j)>1:
                a=0
                for x in range(len(j)-1):
                    a=abs(j[x]-j[x+1])
                    if a<=k:
                        return True
        return False
        '''if len(res)==0 or max(res)>k:
            return False
        else:
            return True'''