# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # save next node before changing pointers
            nxt = curr.next

            # reverse the pointer
            curr.next = prev

            # move pointers forward
            prev = curr
            curr = nxt

        return prev


'''
Logic:
use two pointers: prev and curr

iterate through the linked list

save the next node before changing any pointers

reverse the current node's next pointer so it points
to the previous node

move both pointers forward

when curr becomes null, prev will be pointing to
the new head of the reversed list

return prev

Pattern:
Linked List Pointer Manipulation

Time Complexity:
O(n)
we visit each node exactly once

Space Complexity:
O(1)
only a few pointers are used regardless of list size

Time to complete problem:
~16 minutes
'''