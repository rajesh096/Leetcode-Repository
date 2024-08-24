class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic = {k:v for k,v in (zip([logs[i][0] for i in range(len(logs))],[[] for i in range(len(logs))]))}
        for i in logs:
            dic[i[0]].append(i[1])
        res=[0]*k
        for i,j in dic.items():
            a=len(set(j))
            res[a-1]+=1
                    
        return res
        