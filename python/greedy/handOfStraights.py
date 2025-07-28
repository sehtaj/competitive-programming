# isNStraightHand(hand: List[int], groupSize: int) -> bool

# Time Complexity: O(n log n), where n = len(hand), due to repeated min() operations.
# Space Complexity: O(n), for storing frequency counts in the hash map.

def isNStraightHand(hand, groupSize):
    n = len(hand)
    if n % groupSize != 0:
        return False

    hp = {}
    for i in hand:
        if i not in hp:
            hp[i] = 1
        else:
            hp[i] += 1

    while hp:
        start = min(hp.keys())
        for i in range(start, start + groupSize):
            if i not in hp:
                return False
            hp[i] -= 1
            if hp[i] == 0:
                del hp[i]

    return True

#edge cases
# 1. Valid straight hands
# isNStraightHand([1,2,3,6,2,3,4,7,8], 3) -> True

# 2. Not divisible by groupSize
# isNStraightHand([1,2,3,4,5], 4) -> False

# 3. Consecutive cards but one missing
# isNStraightHand([1,2,4,5,6], 3) -> False

# 4. Duplicate values with valid grouping
# isNStraightHand([1,2,2,3,3,4], 3) -> True

# 5. Single group case
# isNStraightHand([10,11,12], 3) -> True

# 6. All identical values, group size > 1
# isNStraightHand([7,7,7,7], 2) -> False