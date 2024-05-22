class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowspeed = 1
        highspeed = max(piles)

        while lowspeed<highspeed:
            currentspeed = (lowspeed+highspeed)//2
            time=0
            for pile in piles:
                time += ceil(pile/currentspeed)

            if time <= h:
                highspeed=currentspeed
            else:
                lowspeed=currentspeed+1
        return lowspeed
