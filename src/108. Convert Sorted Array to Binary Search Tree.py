from collections import deque
from math import ceil
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def __str__(self):
        return f"{self.val=}"


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        stack = deque()
        used_index = set()

        current_node = TreeNode(
            val=nums[len(nums) // 2]
        )
        used_index.add(len(nums) // 2)
        head = current_node

        stack.append((0, len(nums) // 2, current_node))
        stack.append((len(nums) // 2, len(nums) - 1, current_node))

        while stack:
            left_pointer, right_pointer, current_node = stack.popleft()
            middle_index = (left_pointer + right_pointer) // 2
            print(middle_index)
            number_for_node = nums[middle_index]

            new_node = TreeNode(
                val=number_for_node
            )
            if not current_node.left:

                current_node.left = new_node
            elif not current_node.right:
                current_node.right = new_node

            used_index.add(middle_index)
            if (left_pointer + middle_index) // 2 not in used_index:
                stack.append((left_pointer, middle_index, new_node))
            if (middle_index + right_pointer + 1) // 2 not in used_index:
                stack.append((middle_index + 1, right_pointer, new_node))

        return head


if __name__ == '__main__':
    Solution().sortedArrayToBST(nums=[-10,-3,0,5,9])