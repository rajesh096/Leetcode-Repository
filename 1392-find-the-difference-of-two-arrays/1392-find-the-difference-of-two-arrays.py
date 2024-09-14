class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l=[]
        res=[]
        for i in nums1:
            if i not in nums2 and i not in l:
                l.append(i)
        res.append(l)
        l=[]
        for i in nums2:
            if i not in nums1 and i not in l:
                l.append(i)
        res.append(l)
        return res