def arr(nums):
    """
    This function checks if any value appears more than once in the given array.
    
    
    It uses a dictionary (hashmap) to keep track of the numbers we have encountered.
    If we encounter the same number again, it means there's a duplicate, and we return True.
    Otherwise, we return False after checking all elements.
    
    Parameters:
    nums (List[int]): A list of integers.
    
    Returns:
    bool: True if there are duplicates, False otherwise.
    """
    
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

