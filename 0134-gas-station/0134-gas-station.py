class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = 0
        gasnow = 0
        index = 0
        for i in range(len(gas)):
            diff=gas[i] - cost[i]
            totalGas += diff
            gasnow +=  diff

            if gasnow < 0:#whenever we run outta gas, next index is the probabal answer.
                gasnow = 0
                index = i + 1

        if totalGas >= 0:
            return index
        else:
            return -1
