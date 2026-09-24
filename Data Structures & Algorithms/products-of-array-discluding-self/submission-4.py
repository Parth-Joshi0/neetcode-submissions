class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1,]
        suffix_prod = [1,]
        output = []
        for i, j in zip(range(1, len(nums)), range(len(nums) - 2, -1, -1)):
            prefix_prod.append(prefix_prod[i-1] * nums[i-1])
            suffix_prod.append(suffix_prod[i-1] * nums[j+1])
        
        suffix_prod.reverse()

        for prefix, suffix in zip(prefix_prod, suffix_prod):
            output.append(prefix * suffix)
        return output