class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        z = dict()
        for x in nums:
            if x in z:
                return True
            z[x] = 0
        return False