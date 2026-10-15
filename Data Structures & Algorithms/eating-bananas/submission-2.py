class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        remaining_hours = h - len(piles)
        k_upper_bound = max(piles)
        if remaining_hours == 0:
            return k_upper_bound

        def count_hours(k):
            hrs = 0
            for pile in piles:
                hrs += (-1 * (pile // (-1 * k)))
            return hrs

        l, r = 1, k_upper_bound
        k = 0
        while l < r:
            k = l + (r-l)//2
            hrs = count_hours(k)
            if hrs > h:
                l = k + 1
            else:
                r = k
        return l