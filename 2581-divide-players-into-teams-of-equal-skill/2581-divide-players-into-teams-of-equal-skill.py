class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i,j=0,len(skill)-1
        ar=[]
        while(i<j):
            ar.append(skill[i]+skill[j])
            i+=1
            j-=1
        if(len(set(ar))>1 and len(skill)!=2):
            return -1
        i,j=0,len(skill)-1
        res=0
        while(i<j):
            res+=(skill[i]*skill[j])
            i+=1
            j-=1
        return res