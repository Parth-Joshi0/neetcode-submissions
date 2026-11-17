class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ans = [[]]
        for num in nums:
            for i in range(len(ans)):
                ans.append(ans[i] + [num])
        return ans