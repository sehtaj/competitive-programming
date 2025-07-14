# reverseList: ListNode -> ListNode

# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(head):
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
    
#edge cases
# 1. Empty list (head is None)                            Expected: None
# 2. Single node list ( 1 -> None)                         Expected: 1 -> None
# 3. Two node list (1 -> 2 -> None)                         Expected: 2 -> 1 -> None
# 4. Multiple nodes (1 -> 2 -> 3 -> 4 -> None)                Expected: 4 -> 3 -> 2 -> 1 -> None
# 5. List with duplicate values (1 -> 2 -> 2 -> 1 -> None)    Expected: 1 -> 2 -> 2 -> 1 -> None