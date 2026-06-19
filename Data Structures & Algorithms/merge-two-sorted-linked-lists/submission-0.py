# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            # Add the smaller node to the merged list
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # Move tail forward
            tail = tail.next

        # Attach any remaining nodes
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next


'''
Logic:
create a dummy node to serve as the start of the merged list

use a tail pointer to build the merged list

while both lists still have nodes:
compare the values at each list's current node
attach the smaller node to the merged list
move the corresponding list pointer forward
move the tail pointer forward

once one list is exhausted,
attach the remaining nodes from the other list

return dummy.next since dummy is just a placeholder

Pattern:
Two Pointers (Linked Lists)

Time Complexity:
O(n + m)
we visit each node from both lists exactly once

Space Complexity:
O(1)
the merge is done in place using existing nodes

Time to complete problem:
~24 minutes
'''