import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = nums[0:k]
        heapq.heapify_max(max_heap)
        res = []
        seen = {}

        for i in range(k):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1

        l, r = 0, k

        while True:
            max_element = max_heap[0]

            if max_element in seen:
                res.append(max_element)
            else:
                while max_heap[0] not in seen:
                    heapq.heappop_max(max_heap)

                res.append(max_heap[0])

            if r == len(nums):
                break

            if seen[nums[l]] != 1:
                seen[nums[l]] -= 1
            else:
                del seen[nums[l]]

            if nums[r] in seen:
                seen[nums[r]] += 1
            else:
                seen[nums[r]] = 1

            heapq.heappush_max(max_heap, nums[r])

            l += 1
            r += 1

        return res