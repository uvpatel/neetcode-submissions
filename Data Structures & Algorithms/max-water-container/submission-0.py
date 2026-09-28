class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxwater = 0

        while(left < right):
            w = right - left
            h = min(heights[right],heights[left])
            currwater = w * h

            maxwater = max(maxwater,currwater)

            if(heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
            
        return maxwater
