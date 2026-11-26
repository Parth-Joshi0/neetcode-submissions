import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]**2 + point[1]**2 # No Need For Squareroot, Cause Minimizing both

        return heapq.nsmallest(k, points, key=distance)
        