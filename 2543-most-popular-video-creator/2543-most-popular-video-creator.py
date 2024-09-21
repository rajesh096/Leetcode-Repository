class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        d1 = {}  
        d2 = {}  
        d3 = {}  
        for i in range(len(ids)):
            if creators[i] not in d1:
                d1[creators[i]] = views[i]
                d2[creators[i]] = ids[i]
                d3[creators[i]] = views[i]  
            else:
                
                if d3[creators[i]] < views[i]:
                    d2[creators[i]] = ids[i]
                    d3[creators[i]] = views[i]  
                elif d3[creators[i]] == views[i] and d2[creators[i]] > ids[i]:
                    d2[creators[i]] = ids[i]  

                d1[creators[i]] += views[i]  

        ma = max(d1.values())  
        res = []
        for creator, total_views in d1.items():
            if total_views == ma:
                res.append([creator, d2[creator]])
        
        return res