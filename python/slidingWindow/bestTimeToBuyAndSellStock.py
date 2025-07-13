# maxProfit: List[int], int -> int

# Time Complexity: O(n)
# Space Complexity: O(1)

def maxProfit(prices):
    l = 0
    r = 1
    maxProfit = 0

    while r < len(prices) :
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = r
        r += 1

    return maxProfit

#edge cases
# maxProfit([1, 2, 3, 4, 5])                    Expected: 4
# maxProfit([5, 4, 3, 2, 1])                    Expected: 0
# maxProfit([3, 3, 3, 3])                       Expected: 0
# maxProfit([7])                                Expected: 0
# maxProfit([1, 5])                             Expected: 4
# maxProfit([5, 1])                             Expected: 0
# maxProfit([1,2,4,2,5,7,2,4,9,0,9])            Expected: 9
