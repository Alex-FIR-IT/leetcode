# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def _get_paths_count(
            self,
            *,
            node: TreeNode,
            target_sum: int,
            path_values: List,
            current_sum: int = 0
    ):
        path_values.append(node.val)
        current_sum += node.val
        paths_count = 0

        if node.left:
            paths_count += self._get_paths_count(
                node=node.left,
                target_sum=target_sum,
                path_values=path_values,
                current_sum=current_sum
            )

        if node.right:
            paths_count += self._get_paths_count(
                node=node.right,
                target_sum=target_sum,
                path_values=path_values,
                current_sum=current_sum
            )

        for current_value in path_values:
            if current_sum == target_sum:
                paths_count += 1

            current_sum -= current_value

        path_values.pop()
        return paths_count


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        return self._get_paths_count(
            node=root,
            target_sum=targetSum,
            path_values=[]
        )
