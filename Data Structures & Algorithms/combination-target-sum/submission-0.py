class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        def dfs(index, remaining, current):
            if index < 0 or remaining < 0:
                return
            if remaining == 0:
                ans.append(current.copy())
                return
            current.append(nums[index])
            dfs(index, remaining-nums[index], current)
            current.pop()
            dfs(index-1, remaining, current)
        dfs(len(nums)-1, target, [])
        return ans