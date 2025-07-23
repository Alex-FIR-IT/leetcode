# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from itertools import count


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = fast_pointer = head

        if not fast_pointer.next:
            return None

        for _ in count():
            if fast_pointer is None or fast_pointer.next is None:
                break

            prev_pointer = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        prev_pointer.next = slow_pointer.next
        slow_pointer.next = None

        return head
