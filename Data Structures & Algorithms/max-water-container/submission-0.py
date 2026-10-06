class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            area = (width * height) if (width * height) > area else area
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return area