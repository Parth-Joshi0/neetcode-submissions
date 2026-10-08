class Solution:
    def trap(self, height: List[int]) -> int:
        max_prefix = []
        max_suffix = [0] * len(height)
        max_found = height[0]
        for level in height:
            max_found = max(max_found, level)
            max_prefix.append(max_found)
            
        max_found = height[-1]
        for i in range(len(height) - 1, 0, -1):
            max_found = max(max_found, height[i])
            max_suffix[i] = max_found
        
        volume = 0
        for pre, suf, level in zip(max_prefix, max_suffix, height):
            x = min(pre, suf)
            if x - level > 0:
                volume += x - level
        return volume