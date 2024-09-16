class Solution:
    def compress(self, chars: List[str]) -> int:
        # d={}
        # for i in chars:
        #     if i not in d:
        #         d[i]=1
        #     else:
        #         d[i]+=1
        # s=""
        # chars.clear()
        # for i,j in d.items():
        #     s+=i
        #     if(j>1):
        #         s+=str(j)
        # chars=list(s)
        # print(chars)
        # return 6
        j=0
        c=0
        s=""
        for i in range(1,len(chars)):
            if(chars[i]==chars[i-1]):
                c+=1
            else:
                c+=1
                s+=chars[j]
                if(c>1):
                    s+=str(c)
                j=i
                c=0
        c+=1   
        s+=chars[j]
        if(c>1):
            s+=str(c)
        chars.clear()
        for i in s:
            chars.append(i)
        
        print(chars)
        return len(chars)