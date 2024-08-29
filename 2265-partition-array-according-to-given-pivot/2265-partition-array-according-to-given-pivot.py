class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l1=[]
        l2=[]
        x=0
        for i in nums:
            if(i<pivot):
                l1.append(i)
            elif(i==pivot):
                x+=1
            else:
                l2.append(i)
        return l1+[pivot]*x+l2