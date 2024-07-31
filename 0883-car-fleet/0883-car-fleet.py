class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        fleets = 0
        maxTime = 0

        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]

        for time in times:
            if time > maxTime:
                maxTime = time
                fleets += 1

        return fleets