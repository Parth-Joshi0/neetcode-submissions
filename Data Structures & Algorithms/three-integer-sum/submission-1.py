class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            target = 0 - nums[i]
            while (l < r):
                current_sum = nums[l] + nums[r]
                if current_sum == target:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif current_sum > target:
                    r -= 1
                else:
                    l += 1
        
        return res