class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        remainder_map = defaultdict(int)
        count = 0

        for tm in time:

            remainder = tm % 60

            complement = (60-remainder)%60

            count += remainder_map[complement]

            remainder_map[remainder]+=1

        return count
