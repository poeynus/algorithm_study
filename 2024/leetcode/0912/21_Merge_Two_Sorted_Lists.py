from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_node = ListNode()
        current_node = new_node
        while list1 and list2:
            if list1.val < list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next

        # 입력으로 들어오는 리스트가 정렬이 되어 있기에 가능 안되어 있으면 불가능함 - 근데 그럼 문제가 아예 다를듯
        if list1:
            current_node.next = list1
        elif list2:
            current_node.next = list2

        return new_node.next


Solution().mergeTwoLists(
    ListNode(1, ListNode(2, ListNode(4, ListNode(5)))),
    ListNode(1, ListNode(3, ListNode(4))),
)
# 이거 왜 easy지 어려운데 ;;;
