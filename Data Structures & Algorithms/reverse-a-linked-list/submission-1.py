# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        new_list = list()

        while curr:
            new_list.append(curr)

            curr = curr.next
        
        if not new_list:
            return None
        
        for i in range(len(new_list)-1, -1, -1):
            curr = new_list[i]
            if i == 0:
                curr.next = None
            else:
                curr.next = new_list[i - 1]

        return new_list[-1]
