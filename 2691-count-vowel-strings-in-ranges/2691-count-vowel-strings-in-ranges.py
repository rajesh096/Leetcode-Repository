class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        arr=[]
        r=0
        vo=['a','e','i','o','u']
        for i in words:
            if(i[0] in vo):
                r+=1
                arr.append(r)
            else:
                arr.append(r)
        res=[]
        print(arr)
        for a,b in queries:
            if(a==0):
                res.append(arr[b])
            elif(b-a==0):
                if(words[1][0] in vo):
                    res.append(1)
                else:
                    res.append(0)
            else:
                res.append(arr[b]-arr[a])
        return res