from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new_node = ListNode()
        new_node.val = head.val
        current_node = new_node

        while head.next:
            if current_node.val != head.next.val:
                current_node.next = head.next
                current_node = current_node.next
            head = head.next
        current_node.next = None
        return new_node


Solution().deleteDuplicates(
    ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None)))))
)

# Input: head = [1,1,2]
# Output: [1,2]

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
