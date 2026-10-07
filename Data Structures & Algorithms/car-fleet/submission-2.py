class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(zip(position, speed))
        times = []
        for pair in sorted_pairs:
            times.append((target - pair[0]) / pair[1])
            
        fleets = 0
        biggest_seen = times[-1] - 1
        stack = []
        
        for i in range(len(times) - 1, -1, -1):
            fleets += 1 if biggest_seen < times[i] else 0
            biggest_seen = max(biggest_seen, times[i])
        
        return fleets