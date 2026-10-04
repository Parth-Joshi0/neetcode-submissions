class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
                continue
            while stack and stack[-1][0] < temperatures[i]:
                tmp = stack.pop()
                ans[tmp[1]] = i - tmp[1]
            stack.append((temperatures[i], i))

        return ans