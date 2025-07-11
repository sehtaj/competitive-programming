# searcMatrix: List[List[int]], int -> bool

# Time Complexity: O(log(m * n)) where m is the number of rows and n is the number of columns of matrix.
# Space Complexity: O(1)

def searchMatrix(matrix, target):
        rows = len(matrix)
        cols =len(matrix[0])

        left= 0
        right = rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            row = mid // cols
            col = mid % cols

            if target > matrix[row][col]:
                left = mid + 1
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                return True
        return False

#edge cases
# searchMatrix([[1]], 1)                                                 Single element match
# searchMatrix([[1]], 0)                                                 Single element, no match
# searchMatrix([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 13)                First element of a row
# searchMatrix([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 4)                 Between two elements
# searchMatrix([[1, 3, 5]], 5)                                           One-row matrix
# searchMatrix([[2], [4], [6], [8]], 6)                                  One-column matrix
# searchMatrix([[2], [4], [6], [8]], 7)                                  Not in one-column matrix
# searchMatrix([[1, 3, 5, 7]], 1)                                        First element
# searchMatrix([[1, 3, 5, 7]], 7)                                        Last element