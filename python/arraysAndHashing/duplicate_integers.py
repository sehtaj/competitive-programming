# findDuplicate: List[int] -> bool

# Time Complexity: O(n)
# Space Complexity: O(n)

def findDuplicate(nums):

    # Create an empty dictionary to track numbers we've seen
    seen = {}
    
    # Loop through each number in the array
    for num in nums:
        # Check if the number is already in the dictionary
        if num in seen:
            return True  # Duplicate found
        
        # Add the number to the dictionary if not found before
        seen[num] = True
    
    return False  # No duplicates found after checking all elements

# Example usage:
# arr([1, 2, 3, 4]) returns False
# arr([1, 2, 3, 2]) returns True

