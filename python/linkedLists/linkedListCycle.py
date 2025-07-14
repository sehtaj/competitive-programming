# hasCycle: ListNode -> bool

# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
#edge cases
# Empty list: (head = None)                             Expected:  False
# Single node, no cycle(1 -> None)                      Expected:  False
# Multiple nodes, no cycle(1 -> 2 -> 3 -> 4 -> None)    Expected:  False
# Multiple nodes with a cycle (1 -> 2 -> 3 -> 4, 1)     Expected:  True

