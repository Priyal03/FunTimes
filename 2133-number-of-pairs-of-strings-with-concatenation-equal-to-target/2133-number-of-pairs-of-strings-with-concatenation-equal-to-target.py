class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        frequency = Counter(nums)
        # print(frequency)
        for k, v in frequency.items():
            if target.startswith(k):
                suffix = target[len(k) :]
                count += v * frequency[suffix]
                if k == suffix:
                    count -= frequency[suffix]
        return count
