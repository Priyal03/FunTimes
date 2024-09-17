class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        remainder_map = {} # Array to store how many times each remainder (0 to 59) has appeared
        count = 0

        for tm in time:

            remainder = tm % 60

            complement = (60-remainder)%60

            if complement in remainder_map:
                count += remainder_map[complement]

            if remainder not in remainder_map:
                remainder_map[remainder]=0
            
            remainder_map[remainder]+=1

        return count
