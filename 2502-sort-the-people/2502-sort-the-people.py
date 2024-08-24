class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {k:v for k,v in (zip(heights,names))}
        heights.sort(reverse=True)
        res=[]
        for i in heights:
            res.append(dic[i])
        print(dic)
        return res