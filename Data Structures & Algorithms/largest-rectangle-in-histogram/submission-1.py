class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                left = stack.pop()

                if len(stack) == 0:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area, heights[left] * width)

            stack.append(i)

        while len(stack) > 0:
            left = stack.pop()

            if len(stack) == 0:
                width = len(heights)
            else:
                width = len(heights) - stack[-1] - 1

            max_area = max(max_area, heights[left] * width)

        return max_area