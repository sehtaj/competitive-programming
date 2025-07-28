# canCompleteCircuit(gas: List[int], cost: List[int]) -> int

# Time Complexity: O(n), where n is the number of gas stations.
# Space Complexity: O(1)

def canCompleteCircuit(gas, cost):
    n = len(gas)
    start, end = n - 1, 0

    tank = gas[start] - cost[start]
    while start > end:
        if tank < 0:
            start -= 1
            tank += gas[start] - cost[start]
        else:
            tank += gas[end] - cost[end]
            end += 1
    if tank >= 0:
        return start 
    else:
        return -1
    
#edge cases
# 1. Only one station and it's possible
# canCompleteCircuit([5], [4]) -> 0

# 2. Only one station and it's not possible
# canCompleteCircuit([3], [4]) -> -1

# 3. Total gas < total cost (not possible)
# canCompleteCircuit([1, 2, 3], [3, 4, 5]) -> -1

# 4. Circuit is possible starting at index 3
# canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) -> 3

# 5. Circuit is not possible even though one start seems viable
# canCompleteCircuit([2,3,4], [3,4,3]) -> -1

# 6. All stations have enough gas individually but not for circuit
# canCompleteCircuit([5,5,5], [6,6,6]) -> -1