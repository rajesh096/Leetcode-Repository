class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        mini = float("inf")
        maxi = 1
        for i in bookings:
            mini=min(mini,i[0])
            maxi = max(maxi,i[1])
        arr = [0]*(n)
        for i in bookings:
            arr[i[0]-1]+=i[2]
            if(i[1]!=maxi):
                arr[i[1]]-=i[2]
        for i in range(1,n):
            if i+1<=maxi:
                arr[i]+=arr[i-1]
        return arr
        