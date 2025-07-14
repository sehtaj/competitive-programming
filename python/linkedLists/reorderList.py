# reorderList: ListNode -> ListNode

# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(head):
        if not head or not head.next:
            return
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head
        second = prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

#edge cases
    # []                     Expected: None
    # [1]                   Expected: 1 -> None
    # [1, 2]                Expected: 1 -> 2 -> None
    # [1, 2, 3, 4]          Expected: 1 -> 4 -> 2 -> 3 -> None
    # [1, 2, 2, 1]          Expected: 1 -> 1 -> 2 -> 2 -> None