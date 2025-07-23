# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd_current_node = head
        even_head = head.next

        even_current_node = even_head

        while even_current_node and even_current_node.next:
            odd_current_node.next, even_current_node.next = even_current_node.next, even_current_node.next.next

            odd_current_node = odd_current_node.next
            even_current_node = even_current_node.next

        odd_current_node.next = even_head

        return head

