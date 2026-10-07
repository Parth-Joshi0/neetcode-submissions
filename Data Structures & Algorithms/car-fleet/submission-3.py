class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))

        fleets = 0
        biggest_seen = 0

        for pos, speed in reversed(cars):
            time = (target - pos) / speed

            if time > biggest_seen:
                fleets += 1
                biggest_seen = time

        return fleets