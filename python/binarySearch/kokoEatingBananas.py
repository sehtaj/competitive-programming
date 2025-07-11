# minEatingSpeed: List[int], int -> int

# Time Complexity: O(nlog m)
# Space Complexity: O(1)

def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2

        totalTime = 0
        for p in piles:
            totalTime = totalTime + (p / k)
        if totalTime <= h:
            res = k
            r = k - 1
        else:
            l = k + 1
    return res

# edge cases
# minEatingSpeed([1], 1)                        -> 1
# minEatingSpeed([1000000], 1000000)           -> 1
# minEatingSpeed([3, 6, 7, 11], 8)             -> 4
# minEatingSpeed([30, 11, 23, 4, 20], 100)     -> 1
# minEatingSpeed([30, 11, 23, 4, 20], 5)       -> 30
# minEatingSpeed([10, 10, 10, 10], 4)          -> 10
# minEatingSpeed([10, 10, 10, 10], 8)          -> 5