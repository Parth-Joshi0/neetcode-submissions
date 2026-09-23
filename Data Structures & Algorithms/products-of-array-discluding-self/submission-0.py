class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        mul_without_zero = 1
        zero_counter = 0
        for num in nums:
            mul *= num
            if num == 0:
                zero_counter += 1
            else:
                mul_without_zero *= num
        output = []
        for num in nums:
            if zero_counter > 1:
                output.append(0)
                continue
            if num != 0:
                output.append(int(mul / num))
            else:
                output.append(int(mul_without_zero))
        return output