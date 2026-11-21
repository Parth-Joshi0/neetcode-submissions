class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(index, remaining, current):
            if remaining == 0:
                ans.append(current.copy())
                return
            if index < 0 or remaining < 0:
                return
            current.append(candidates[index])
            dfs(index-1, remaining-candidates[index], current)
            current.pop()
            while index > 0 and candidates[index] == candidates[index-1]:
                index -= 1
            dfs(index-1, remaining, current)
        dfs(len(candidates)-1, target, [])
        return ans