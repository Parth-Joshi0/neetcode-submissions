class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(current, used):
            if len(current) == len(nums):
                res.append(current.copy())
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                current.append(nums[i])
                dfs(current, used)
                current.pop()
                used.remove(i)
        dfs([], set())
        return res