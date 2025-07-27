# minRefuel(target: int, startFuel: int, stations: List[List[int]]) -> int

# Time Complexity: O(n^2), where n is the number of stations
# Space Complexity: O(n^2), for the DP table

def minRefuel(target, startFuel, stations):
    n = len(stations)
    dp = []
    for i in range(n + 1):
        dp.append([0] * (n + 1))
    
    for i in range(n + 1):
        dp[i][0] = startFuel

    for i in range(1, n + 1):
        position, fuel = stations[i - 1]
        for j in range(i + 1):
            if dp[i - 1][j] >= position:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])

            if j > 0 and dp[i - 1][j - 1] >= position:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + fuel)

    for j in range(n + 1):
        if dp[n][j] >= target:
            return j

    return -1

# edge cases
# 1. No refueling needed
# minRefuel(100, 100, [])  -> 0

# 2. One station exactly where fuel runs out
# minRefuel(100, 50, [[50, 50]])  -> 1

# 3. Not enough fuel and no stations
# minRefuel(100, 1, [])  -> -1

# 4. Multiple stations, still can’t reach
# minRefuel(1000, 1, [[10, 10], [20, 20], [30, 30]])  -> -1

# 5. One good station makes it possible
# minRefuel(100, 10, [[10, 90]])  -> 1

# 6. Skipping stations gives optimal result
# minRefuel(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]])  -> 2