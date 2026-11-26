from collections import defaultdict, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)

        for task in tasks:
            counts[task] += 1

        heap = [[-occurrence, task]
                for task, occurrence in counts.items()]

        heapq.heapify(heap)

        queue = deque([None] * n)
        time = 0

        while heap or any(queue):
            time += 1

            if heap:
                task = heapq.heappop(heap)
                task[0] += 1

                if task[0] < 0:
                    queue.append(task)
                else:
                    queue.append(None)
            else:
                queue.append(None)

            item = queue.popleft()

            if item:
                heapq.heappush(heap, item)

        return time