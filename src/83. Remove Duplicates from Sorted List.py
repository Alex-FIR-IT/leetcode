# Definition for singly-linked list.#
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current_element = head.next

        while current_element is not None and current_element.next is not None:
            if current_element.val == current_element.next.val:
                current_element.next = current_element.next.next

            current_element = current_element.next

        return head