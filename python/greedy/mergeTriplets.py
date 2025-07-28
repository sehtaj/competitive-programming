# mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool

# Time Complexity: O(n), where n = len(triplets)
# Space Complexity: O(1), only constant space used for flags

def mergeTriplets(triplets, target):
    t1, t2, t3 = target

    foundX = False
    foundY = False
    foundZ = False

    for triplet in triplets:
        a = triplet[0]
        b = triplet[1]
        c = triplet[2]

        if a <= t1 and b <= t2 and c <= t3:
            if a == t1:
                foundX = True
            if b == t2:
                foundY = True
            if c == t3:
                foundZ = True

    if foundX and foundY and foundZ:
        return True
    else:
        return False
    
# 1. Basic match from three triplets
# mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]) -> True

# 2. No triplet satisfies condition
# mergeTriplets([[3,4,5],[4,5,6]], [3,4,5]) -> False

# 3. Only one triplet equals target
# mergeTriplets([[3,4,5]], [3,4,5]) -> True

# 4. Values too large to be used
# mergeTriplets([[4,4,4],[5,5,5]], [3,3,3]) -> False

# 5. One dimension can't be matched
# mergeTriplets([[3,4,5],[2,7,2],[2,3,5]], [2,7,5]) -> False

# 6. Multiple valid options, but only one full match possible
# mergeTriplets([[2,5,3],[1,7,4],[2,7,5]], [2,7,5]) -> True