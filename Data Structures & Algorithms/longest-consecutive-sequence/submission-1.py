class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        start = {}
        end = {}
        for num in nums:
            if num in seen:
                continue
            else:
                seen.add(num)
            has_left = num + 1 in start
            has_right = num - 1 in end
            
            if has_left and has_right:
                start_num = end[num - 1]
                end_num = start[num + 1]

                del start[start_num]
                del end[num - 1]

                del start[num + 1]
                del end[end_num]

                start[start_num] = end_num
                end[end_num] = start_num
                
            elif has_left:
                end_num = start.pop(num+1)
                start[num] = end_num
                end[end_num] = num
                
            elif has_right:
                start_num = end.pop(num - 1)
                end[num] = start_num
                start[start_num] = num
                
            else: 
                start[num] = num
                end[num] = num
            
        longest = 0 
        for num in start:
            lenght = start[num] - num
            if lenght > longest:
                longest = lenght
        if seen:   
            return longest + 1
        return longest
        