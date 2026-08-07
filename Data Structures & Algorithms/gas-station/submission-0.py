class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalgas = sum(gas)
        totalcost = sum(cost)

        if totalgas< totalcost:
            return -1
        currgas = 0
        start = 0

        for i in range(len(gas)):
            currgas += gas[i] - cost[i]
            if currgas<0:
                start = i+1
                currgas = 0
            
        return start