from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pioneer = head
        follower = head

        while pioneer is not None and pioneer.next is not None:
            pioneer = pioneer.next.next
            follower = follower.next
        return follower


# GPT가 가장 최적의 성능이래
# 약간 문제에서 하정이 있는데 output이 [3, 4, 5]이지만 3이 나와야 함 leet code의 방식이래,
# input도 내가 만든 것 처럼 만들어야 해 leet code의 linked list 풀 때 어떻게 해야 하는지 알았음

"""
It's just Leetcode's way of representing LinkedList nodes. Below is an explanation that might help you.
It is because nodes are connected to each other, and the question asks to return the "middle node", not the "value". So, for example head = [1,2,3,4,5], 
then the output should be [3,4,5], instead of just 3 because we are returning a node whose value will be 3 and that 3 points to 4 and 4 points to 5. 
So, when we return a node whose value is 3 we will also have access to nodes whose values are 4 and 5.
So, you are not really returning an array, the array represented as output is just an implicit representation of nodes that are connected to each other.
"""

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
Solution().middleNode(head)

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
