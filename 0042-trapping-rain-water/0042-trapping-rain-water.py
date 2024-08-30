class Solution(object):
    def trap(self, height):
        left = 0 
        right = len(height)-1
        lm = 0
        rm = 0
        res = 0
        while(left<right):
            if(height[left]<=height[right]):
                if(height[left]>lm):
                    lm = height[left]
                else:
                    res += lm-height[left]
                left += 1
            else:
                if(height[right]>rm):
                    rm = height[right]
                else:
                    res += rm - height[right]
                right -= 1
        return res