# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val=}, {self.next=}"


class Solution:
    @staticmethod
    def _reverse_linked_list(head: ListNode) -> ListNode:

        current_node = head
        previous_node = None

        while current_node.next:
            previous_node, current_node.next, current_node = current_node, previous_node, current_node.next

        current_node.next = previous_node
        return current_node

    def pairSum(self, head: Optional[ListNode]) -> int:

        slow_pointer = fast_pointer = head

        while fast_pointer and fast_pointer.next:
            previous_slow_pointer = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        right_subarray_node = self._reverse_linked_list(slow_pointer)
        left_subarray_node = head
        max_twin_sum = 0

        while right_subarray_node:
            max_twin_sum = max(max_twin_sum, left_subarray_node.val + right_subarray_node.val)
            left_subarray_node = left_subarray_node.next
            right_subarray_node = right_subarray_node.next

        return max_twin_sum

if __name__ == '__main__':
    print(Solution().pairSum(head=ListNode(val=5,
                                           next=ListNode(val=4,
                                                         next=ListNode(val=2,
                                                                       next=ListNode(val=1))))))