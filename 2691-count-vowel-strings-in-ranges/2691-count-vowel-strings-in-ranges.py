class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        arr=[0]
        r=0
        vo=['a','e','i','o','u']
        for i in words:
            if(i[0] in vo) and (i[-1] in vo):
                r+=1
                arr.append(r)
            else:
                arr.append(r)
        res=[]
        print(arr)
        for a,b in queries:
            
            res.append(arr[b+1]-arr[a])
            # elif(b-a==0):
            #     if(words[1][0] in vo):
            #         res.append(1)
            #     else:
            #         res.append(0)
            # else:
            #     res.append(arr[b]-arr[a])
        return res