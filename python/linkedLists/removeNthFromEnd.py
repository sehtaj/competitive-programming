# removeNthfromEnd: ListNode, int -> ListNode

# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthfromEnd(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next

# Input: [1], n = 1                Expected: []                   
# Input: [1, 2], n = 1             Expected: [1]                  
# Input: [1, 2], n = 2             Expected: [2]                  
# Input: [1, 2, 3], n = 3          Expected: [2, 3]           
# Input: [1, 2, 3], n = 2          Expected: [1, 3]              
# Input: [1, 2, 3], n = 1          Expected: [1, 2]             
# Input: [1, 2, 3, 4, 5], n = 5    Expected: [2, 3, 4, 5]         
# Input: [1, 2, 3, 4, 5], n = 3    Expected: [1, 2, 4, 5]        
# Input: [1, 2, 3, 4, 5], n = 1    Expected: [1, 2, 3, 4]        
# Input: [], n = 1                 Expected: []        


