class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict().fromkeys(set(nums), 0)

        for num in nums: 
            count[num] += 1

        x = [[] for _ in range(len(nums))]

        for num in count:
            x[count[num] - 1].append(num)

        answer = []

        for i in range(len(x) - 1, -1, -1):
            for num in x[i]:
                answer.append(num)

                if len(answer) >= k:
                    return answer

        return answer