# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        current_node = head
        previous_node = None

        while current_node and current_node.next:
            previous_node, current_node.next, current_node = current_node, previous_node, current_node.next

        current_node.next = previous_node

        return current_node
