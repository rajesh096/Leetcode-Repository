class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        dic = {k:v for k,v in (zip(senders,[0 for i in range(len(senders))]))}
        for i in range(len(messages)):
            n=len(messages[i].split())
            dic[senders[i]]+=n
        res=""
        x=max(dic.values())
        for i,j in dic.items():
            if j==x:
                if i>=res:
                    res=i
                 
        return res