class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s=0
        e=len(arr)-1
        pos=0
        while(s<=e):
            mid=(s+e)//2
            a=arr[mid+1] if mid+1!=len(arr) else float("inf")
            b=arr[mid-1] if mid!=0 else float("-inf")
            if(arr[mid]>b and arr[mid]>a):
                pos=mid
                break
            elif(arr[mid]>a):
                e=mid-1
                pos=mid
            else:
                s=mid+1
        return pos
        