# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []
        stack = []
        current = root

        while stack and current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)

            current = current.right

        return result


root = TreeNode(1)  # 루트 노드 1 생성
root.left = TreeNode(2)  # 왼쪽 자식 2
root.right = TreeNode(3)  # 오른쪽 자식 3
root.left.left = TreeNode(4)  # 2의 왼쪽 자식 4
root.left.right = TreeNode(5)  # 2의 오른쪽 자식 5
root.right.right = TreeNode(8)  # 3의 오른쪽 자식 8
root.left.right.left = TreeNode(6)  # 5의 왼쪽 자식 6
root.left.right.right = TreeNode(7)  # 5의 오른쪽 자식 7
root.left.right.right.right = TreeNode(9)  # 7의 오른쪽 자식 9

Solution().inorderTraversal(root)

# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]
