# addTwoNumbers: ListNode, ListNode -> ListNode

# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = 0
            v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next

            if l2:
                v2 = l2.val
                l2 = l2.next

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next
    
#edge Cases:
# Both lists are empty (None, None)               Expected: None
# One list is empty (None, 1 -> 2 -> 3)           Expected: 1 -> 2 -> 3
# No carry needed (2 -> 3, 4 -> 1)                Expected: 6 -> 4
# Carry exists (5 -> 5, 5 -> 5)                   Expected: 0 -> 1 -> 1(because 55 + 55 = 110)
# Different lengths (9 -> 9 -> 1, 1)              Expected: 0 -> 0 -> 2
# Carry after last node (9 -> 9, 1)               Expected: 0 -> 0 -> 1
# Long carry chain (9 -> 9 -> 9, 1)               Expected: 0 -> 0 -> 0 -> 1