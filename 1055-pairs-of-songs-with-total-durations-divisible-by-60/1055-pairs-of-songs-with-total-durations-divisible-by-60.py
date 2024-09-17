class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        remainder_count = [0] * 60 # Array to store how many times each remainder (0 to 59) has appeared
        count = 0

        for i in range(n):

            remainder = time[i] % 60

            if remainder == 0:
                curr = 0
            else:
                curr = 60 - remainder # We want to find a complement remainder such that (remainder + complement) % 60 == 0
            

            count += remainder_count[curr] #since we can only consider for i<j
            
            remainder_count[remainder] += 1 # the current song's remainder

        return count
