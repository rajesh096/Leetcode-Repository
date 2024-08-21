class Solution:
    def groupThePeople(self, gr: List[int]) -> List[List[int]]:
        s=set(gr)
        res=[]
        dic = {k:v for k,v in (zip(s,[[] for _ in range(len(gr))]))}
        for i in range(len(gr)):
            dic[gr[i]].append(i)
        for i,j in dic.items():
            if i==len(j):
                res.append(j)
            else:
                for k in range(0,len(j)-i+1,i):
                    res.append(j[k:k+i]) 
        return res