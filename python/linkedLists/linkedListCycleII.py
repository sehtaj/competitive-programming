# detectCycle: ListNode -> ListNode

# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                 break
        else: 
            return None  

        while head != slow:
            head, slow = head.next, slow.next
        return head
    
#edge cases
# Input: []                                         Expected: None                     
# Input: [1], no cycle                              Expected: None                     
# Input: [1] -> points to self                      Expected: Node(1)                  
# Input: [1 -> 2], no cycle                         Expected: None                  
# Input: [1 -> 2], with 2 -> 1                      Expected: Node(1)                  
# Input: [1 -> 2 -> 3], with 3 -> 2                 Expected: Node(2)                 
# Input: [1 -> 2 -> 3 -> 4], 4 -> 2                 Expected: Node(2)         
# Input: [1 -> 2 -> 3 -> 4 -> 5], no cycle          Expected: None            
# Input: [1 -> 2 -> 3], with 3 -> 3                 Expected: Node(3)         
# Input: [1 -> 2 -> 3 -> 4 -> 2], 4 -> 2            Expected: Node(2)              