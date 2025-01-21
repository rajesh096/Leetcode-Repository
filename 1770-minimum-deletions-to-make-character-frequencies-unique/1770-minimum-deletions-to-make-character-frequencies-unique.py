class Solution:
    def minDeletions(self, s: str) -> int:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        dic = dict(sorted(dic.items(), key=lambda item: item[1],reverse=True))
        res = 0
        arr = []
        for i in dic.values():
            if i not in arr:
                arr.append(i)
            else:
                while(i in arr and i>0):
                    res +=1
                    
                    i-=1
                if(i>0):
                    arr.append(i)
        return res