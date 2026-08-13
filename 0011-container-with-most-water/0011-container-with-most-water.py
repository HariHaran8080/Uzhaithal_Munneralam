class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        result=0
        while left<right:
            d=right-left
            m=min(height[left],height[right])
            f=d*m
            if f>result:
                result=f
            elif height[left]>height[right]:
                right=right-1
            else:
                left=left+1
        return result
