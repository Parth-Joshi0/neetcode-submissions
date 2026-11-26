import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        output = heapq.nlargest(k, nums)
        return output[-1]
        