class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        u=edges[0][0]
        v=edges[0][1]
        for i in range(1,len(edges)):
            if(u==edges[i][0] or u ==edges[i][1]):
                return u
            else:
                return v