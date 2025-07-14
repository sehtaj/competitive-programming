# mergeTwoLists: ListNode, ListNode -> ListNode

# Time Complexity: O(n + m), where n is the length of l1 and m is the length of l2
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

#edge cases
# Both lists are empty: (l1 = None, l2 = None)                    Expected: None
# One list is empty: (l1 = None, l2 = 1)                          Expected: 1
# One list is longer than the other: (l1 = 1 -> 4 -> 5, l2 = 2)   Expected: 1 -> 2 -> 4 -> 5
# Lists with duplicate values: (l1 = 1 -> 3, l2 = 1 -> 2)         Expected: 1 -> 1 -> 2 -> 3
