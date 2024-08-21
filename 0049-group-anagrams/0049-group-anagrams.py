class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic =dict()
        res=[]
        for i in range(len(strs)):
            a=sorted(strs[i])
            b=''.join(a)
            dic[b]=[]
        for i in strs:
            a=sorted(i)
            b=''.join(a)
            dic[b].append(i)
        for i,j in dic.items():
            res.append(j)
        res.sort()

        return res