class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(curr, index):
            res.append(curr.copy())
            if len(curr) == len(nums):
                return
            if index >= len(nums):
                return

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()
                

        backtrack([], 0)
        return res                    
