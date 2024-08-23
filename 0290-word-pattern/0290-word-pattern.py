class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l= list(s.split())
        if len(s)==0 or (len(set(l))==1 and len(pattern)!=1) or (len(l)!=len(pattern)):
            return False
        else:
            a=[]
            dic={k:v for k,v in (zip(set(pattern),[[] for i in range(len(pattern))]))}            
            for i in range(len(pattern)):
                dic[pattern[i]].append(l[i])
            for i,j in dic.items():
                for k in range(len(j)-1):
                    if j[k]!=j[k+1]:
                        return False
                if j[0] not in a:
                    a.append(j[0])
                else:
                    return False

            return True
                
         