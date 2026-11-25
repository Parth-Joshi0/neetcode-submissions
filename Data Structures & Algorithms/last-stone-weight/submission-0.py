import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:

            stone_x = -heapq.heappop(heap)
            stone_y = -heapq.heappop(heap)

            if stone_x == stone_y:
                continue
            
            stone_x -= stone_y
            heapq.heappush(heap, -stone_x)
        
        if heap:
            return -heap[0]
        return 0